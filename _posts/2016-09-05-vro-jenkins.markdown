---
layout: post
title: Using VMware vRealize Orchestrator to run a Jenkins job and get the results
date: '2016-09-05 19:10:48'
tags:
    - vware-vrealize-orchestrator
    - script
---

![jenkins](/assets/jenkins.png){: .center-image }

[VMware vRealize Orchestrator](http://www.vmware.com/products/vrealize-orchestrator.html) (vRO) is pretty flexible, but there are times when you still need to execute a job on [Jenkins](https://jenkins.io/). <!--more--> It's pretty easy to [create a Jenkins job which you can run by hitting a specific URL](https://wiki.jenkins-ci.org/display/JENKINS/Remote+access+API) and vRO can do this in a couple of lines of JavaScript:-

```
urlObject = new URL(yourJobUrl);
urlObject.getContent();
```

This works well enough, assuming that you don't need to wait on the job to complete and/or check that it completed successfully. If you do need to to do either of those things, then you need to use vRO's REST capabilities. 

In this article, I'll describe how to set up and use a Jenkins REST host in vRO. Before we start, I'm assuming you're familiar (at least to some degree) with Jenkins, vRO and JavaScript.

## Running a simple Jenkins (no build parameters)

### Create the example Jenkins job

1. I created a simple Jenkins job, which requires no build parameters. It returns a single cat fact from [catfacts-api.appspot.com](http://catfacts-api.appspot.com). To do this, I'm using the [PowerShell plug-in](https://wiki.jenkins-ci.org/display/JENKINS/PowerShell+Plugin) to run a single-line of PowerShell (`((Invoke-Webrequest -Uri "http://catfacts-api.appspot.com/api/facts?number=1" -UseBasicParsing).content | ConvertFrom-Json).facts`). What the job does isn't really important though, I just wanted something slightly more interesting than a random number generator, or a "Hello World!".
2. Under the **Build triggers** section, make sure that **Trigger builds remotely (e.g., from scripts)** is set. You should also [create an authentication token](http://randomkeygen.com).
3. **Build** the job in Jenkins to confirm that it works, the console output should look something like this:-

```
Started by user Neise, Ben
Building remotely on ######## (#################################) in workspace #:\Resources\jenkins\workspace\###########\Generate Cat Fact
[Generate Cat Fact] $ powershell.exe "& 'C:\Users\############\AppData\Local\Temp\#####################.ps1'"
Cat families usually play best in even numbers. Cats and kittens should be acquired in pairs whenever possible.
Finished: SUCCESS
```

### Create the Orchestrator REST Host & REST Operation

We need to create a REST host object representing the Jenkins server, and a REST operation representing the specific job.

1. Run the vRO workflow **Library\Configuration\Add a REST host** and configure **Host Properties** as follows:
 - Name: `My Jenkins Server`
 - URL: `http://:8080/jenkins/` (use the URL and port of your Jenkins server)
 - Connection timeout (seconds): `30.0` (you may wish to tune this for your specific requirements, but I'm leaving it as the default for now)
 - Operation timeout (seconds): `60.0` (you may wish to tune this for your specific requirements, but I'm leaving it as the default for now)
 - Configure **Proxy settings**
 - Use Proxy: `No` (Unless you have a proxy!)
 - Configure `Host Authentication`
 - Host's authentication type: `NONE`
2. Now run the Orchestrator workflow **Library\Configuration\Add a REST Operation and configure **Operation properties** as follows:
 - Parent host: Select your new REST host `My Jenkins Server` (or whatever you called it)
 - Name: `Generate cat fact`
 - Template URL: This should be the URL to your job. You should be able to see this below the **Trigger builds remotely (e.g., from scripts)** section in the Jenkins job configuration. It will look something like `/job/Generate%20Cat%20Fact/build?token=xxxxxxxxxxxxxxxxxxxxxxxxx`
 - HTTP Method: `GET`
3. You can test this operation by right-clicking, then selecting **Run workflow > Invoke a REST operation > Submit.** It should run without errors (but it won't wait for the Jenkins job to complete, or give you any output)

### Create the vRO Workflow which will run the Jenkins job, and get the results

Now we need an Orchestrator workflow which runs the operation, waits for it to complete and displays the status and output.

1. Using the Orchestrator client, create a new workflow. I'm going to call mine **Cat fact**
2. The workflow needs a single attribute of type `REST:RESTOperation`, this should be set to your REST operation. My operation is `Generate cat fact` and I named this attribute `generateCatFact`.
3. The workflow needs a single scriptable task, the `REST:Operation` attribute named `generateCatFact` should be bound as an input. The script should be something like this.

```javascript
var jenkinsPollingIntervalMS = 1000;
var buildURL = "";
var buildResult = null;

/*
    Create the request object. The two paramaters are:-
     - An array of values for the URL template paramaters. We have none, so this is null
     - Any content for POST or PUT operations. Ours is a GET, so this is also nulll
*/
var objRESTRequest = generateCatFact.createRequest(null,null);
// Execute the REST operation
var objRESTResponse = objRESTRequest.execute();
System.debug("Status code: " + objRESTResponse.statusCode);
// The location property gives us the URL of the queue item
System.debug("Location: " + objRESTResponse.getAllHeaders().get("Location"));

// Wait for job to be queued by looking for an "executable" property on the response
while (buildURL === ""){
    var url = objRESTResponse.getAllHeaders().get("Location") + "api/json";
    var urlObject = new URL(url);
    result = urlObject.getContent() ;
    //System.debug(result);
    var objResult = JSON.parse(result);
    if (objResult.hasOwnProperty("executable")){
        System.debug(objResult.executable.url);
        buildURL = objResult.executable.url;
    }
    System.sleep(jenkinsPollingIntervalMS);
}

// Now that the job's queued, we need to wait for it to be completed
while (buildResult === null){
    url = buildURL + "api/json";
    var urlObject = new URL(url);
    var result = urlObject.getContent() ;
    var objResult = JSON.parse(result);
    System.debug(result);
    System.debug("Build result:" + buildResult);
    buildResult = objResult.result;
    System.sleep(jenkinsPollingIntervalMS);
}

url = objResult.url + "consoleText";
var urlObject = new URL(url);
result = urlObject.getContent();
// The result is the actual console output.
System.log(result);
System.debug("Build Result: " + buildResult);
```

1. When run, the output should look something like this:-
```
[2016-01-05 10:17:10.850] [D] Status code: 201 [2016-01-05 10:17:10.850] [D] Location: http://##################:8080/jenkins/queue/item/27553/ [2016-01-05 10:17:18.995] [D] http://##################/jenkins/job/Orchestration/job/Generate%20Cat%20Fact/6/ [2016-01-05 10:17:20.035] [D] {"actions":[{"causes":[{"shortDescription":"Started by remote host ##.##.##.##"}]}],"artifacts":[],"building":true,"description":null,"duration":0,"estimatedDuration":2304,"executor":{},"fullDisplayName":"Orchestration ┬╗ Generate Cat Fact #6","id":"2016-01-05_10-17-18","keepLog":false,"number":6,"result":null,"timestamp":1451989038408,"url":"http://##################/jenkins/job/Orchestration/job/Generate%20Cat%20Fact/6/","builtOn":"########","changeSet":{"items":[],"kind":null},"culprits":[]} [2016-01-05 10:17:20.035] [D] Build result:null [2016-01-05 10:17:21.074] [D] {"actions":[{"causes":[{"shortDescription":"Started by remote host ##.##.##.##"}]},{}],"artifacts":[],"building":false,"description":null,"duration":2233,"estimatedDuration":2300,"executor":null,"fullDisplayName":"Orchestration ┬╗ Generate Cat Fact #6","id":"2016-01-05_10-17-18","keepLog":false,"number":6,"result":"SUCCESS","timestamp":1451989038408,"url":"http://##################/jenkins/job/Orchestration/job/Generate%20Cat%20Fact/6/","builtOn":"########","changeSet":{"items":[],"kind":null},"culprits":[]} [2016-01-05 10:17:21.074] [D] Build result:null [2016-01-05 10:17:22.114] [I] Started by remote host ##.##.##.## Building remotely on ######## (############# ######### ####### ##########) in workspace E:\Resources\jenkins\workspace\Orchestration\Generate Cat Fact [Generate Cat Fact] $ powershell.exe "& 'C:\Users###########\AppData\Local\Temp\hudson6191574617805554949.ps1'" The life expectancy of cats has nearly doubled since 1930 - from 8 to 16 years. Finished: SUCCESS [2016-01-05 10:17:22.114] [D] Build Result: SUCCESS
```

## Running a more complex Jenkins job with build parameters


### Create the Jenkins job

1. I created another job, using the same [cat facts api](http://catfacts-api.appspot.com), but this time it allows multiple cat facts to be returned.
2. The job has a single string parameter named `facts`, this parameter is used in the job like so `((Invoke-Webrequest -Uri "http://catfacts-api.appspot.com/api/facts?number=:$env:facts" -UseBasicParsing).content | ConvertFrom-Json).facts`


### Create the vRO REST Host & REST Operation

1. We're going to use the same REST host object, but create a new operation.
2. Run the Orchestrator workflow **Library\Configuration\Add a REST Operation** and configure **Operation properties**
 - Parent host: Select your REST host
 - Name: `Generate cat facts`
 - Template URL: As before, you can get the URL from under the **Trigger builds remotely** section on the Jenkins job configuration. You'll need to also pass any parameters. In the example, we need to pass `facts`. The Orchestrator dialog explains the placeholder syntax requires that runtime parameters be surrounded by curly-braces, so you should end up with something like this `/job/Generate%20Cat%20Facts/buildWithParameters?facts={facts}&token=xxxxxxxxxxxxxxxxxxxxxx`
 - HTTP Method: `GET`
3. You can test this operation by right-clicking, then selecting **Run workflow > Invoke a REST operation > Submit**. It should run without errors (but it won't wait for the Jenkins job to complete, or give you any output)


### Create the vRO Workflow which will run the Jenkins job, and get the results

1. Duplicate the **Cat fact** Orchestrator workflow we created above (on the right-click menu), name it **Cat facts**, and make the following changes:
 - Create a single input called `facts` of type `Number`.
 - Bind `facts` to the `Scriptable task`. The scriptable task should have two inputs  - `facts` (a `Number`), and `generateCatFacts` (a `REST:RESTOperation`).
 - In the scriptable task, change the line `var objRESTRequest = generateCatFact.createRequest(null,null);` to `var objRESTRequest = generateCatFact.createRequest([facts],null);`, this will now pass the REST operation an array containing a single element (the facts input). If you have multiple inputs, you simply add them as items in this array in the order in which they are required in the URL (which is defined in the REST operation).
5. Run the new vRO job, and enter a valid input (for [this API](https://catfacts-api.appspot.com/doc.html), something between 1-100). You should now get the Jenkins console output in your Orchestrator console. Obviously, outputting the job result and console output to screen is of limited use, but you are now able to parse those values and bind them to workflow outputs.