---
layout: page
title: How I use Jira
summary: An opinionated guide on using JIRA
---

# Introduction

This page gives some hints and tips on using JIRA as well as an opinionated view on how to set up work. This is a guide to using JIRA, not administering JIRA.


# Requirements

* I need to be able to see what's being worked on (and by whom)
* The system shouldn't be so complex that it discourages people from using it


# General hints and tips

* Much like documentation, it's better to have information in JIRA in the wrong place, or under the wrong issue type than it is not to have the information in Jira. Generally things can be changed, and shuffled as required. So don't worry too much about structure, and just make sure to log, and update, issues.
* Tagging people will notify them that they've been mentioned!
* This also means that you can assign anyone in Sky to an issue and create dependencies on other people's projects, which is useful
* Limit the number of fields to keep issue-creation simple
* Everything in Jira is an Issue. Issues can be changed between types (Bug, User Story, etc.).
* You can even promote subtasks to issues or demote change issues to subtasks. 
* You can move issues between projects
* You can create Links between any an all task types by using the **Link** option in the **More** menu drop down. You can then select from a myriad of linking options and the issue you want to link it to and add an optional comment on why they are linked. 
    * _Blocks_ or _Depends on_? there's a good break-down [here](https://pm.stackexchange.com/questions/26451/whats-difference-between-depends-on-and-is-blocked-by-relations-between-iss). In short.... 
* Dependencies are used for known or planned activities
* Blocks are used for unexpected activities
* You can Clone issues via the More menu. This is handy for creating multiple similar stories (i.e., a story for RHEL 7 and all it's subtasks can be cloned to a story for RHEL 8, where the tasks would be analogous)
* You can click issues to flag them, which turns them orange. This seems useful, but I haven't quite worked out what to do with it.

# Issues

Everything in JIRA is an Issue, but there are different kinds of issues.

## Issue types

### Epic
Collection of tasks and stories which define an outcome.
This is typically a high level deliverable, for example a Project or a milestone, with some sort of funding, and maybe a PM or cost code.
These are typically the kinds of high-level achievements that we'd present to management at the end of the year.
Think of things that need reported at Ross, Bryan (Engineering Platform Manager) or Tawfik, Rabeh's level or higher
Once an Epic is "mostly done", it can be removed from the backlog by selecting Mark as Done, which is different to completing it

### User Story
User stories are effectively deliverables. They might be something like "Customer would like a custom Debian image".
The idea behind calling them a user story is to keep the customer requirements in focus, rather than the solution
Would typically contain a number of subtasks under this (i.e., "Customer needs to define required packages", "Image should be pen-tested by Security"). When the tasks are complete, the "Story" is delivered.
User stories are typically the level at which the Technical Lead should track and report

### Decision
Useful when a task is awaiting someone deciding something.
You can create a Decision, assign it to them, or open it to the team, and have the outcome tracked

### Bug
Should be used for unplanned work
Unfortunately, bugs can't be assigned to stories, so try to add links ("... blocks ...") to the affected stories, or subtasks

### Task
Typically used by any team members to describe other planned, non-story work. If you're not sure what the Issue type should be, Task is a fairly good place to start!
For example "Tidy up networks in Development" isn't really worth a story, as there are no subtasks.
If these do get more complex, then they can be converted to stories, and subtasks added
Tasks should take between 1 hour & 3 days.

### Subtasks
Subtasks can be tested under any of the Issue types above.
Subtask name should make sense on their own, people won't always be viewing the subtask in the context of it's parent
You can prefix subtasks when you're creating multiple
Do not appear on BigGantt by default, but can be added using Settings > Tasks > Task Structure
If you're adding subtasks to a task, consider making it a User Story. When all of the sub tasks are complete, the user story is finished.

### Example hierarchy
Here's an example Epic which describes the plot of  the first two Terminator movies.

Epic - Prevent the machines from destroying humanity
User Story - Sarah Connor should have a child to led the resistance
Subtask - Find a time machine
Subtask - Send Kyle Reese  back to 1984
Subtask - Save Sarah Conor
User Story - Kyle Reese should survive to lead the resistance
Subtask - Find another time machine
Subtask - Send a repurposed Model-101 Terminator back to 1995
Subtask - Save John Connor
Decision - Should we try to destroy SkyNet in the past by killing Miles Dyson?
Bug - Users travelling through time will appear in the target timeline without clothes or weapons
Remember, that this isn't definitive. Maybe Terminator and Terminator 2 should have been separate Epics?

## Issue titles
Issues should have an actionable title

Bad: Terminator is naked
No indication why this is an issue

Better: Terminator should not be naked
Describes the problem

Best: Terminator needs your clothes, your boots and your motorcycle
Describes what needs done

## Issue States
### In progress
The issue is actively being worked

### On Hold
The issue is blocked

You should not use this state for "I was working on this, but now I'm busy with something else". Either leave that issue as In Progress, or ensure it's up-to-date, and mark it as to-do again

### Complete
The issue is complete

# Handy JQL
The easiest way to use these is to go to **Issues** > **Search for issues**, and paste in the command.

### List all issues and tasks in an epic
`"Epic Link" = VDCTEAM-420 OR parent in ("VDCTEAM-420")`

### List all issues updated by a user in the last 8 days
`issuekey IN updatedBy(currentUser(), "-8d")`

### Show me all issues that I've been mentioned in within the last 7 days
`text ~ currentUser() AND updatedDate >= -7d ORDER BY updated DESC`

### Show me all the issues I'm watching
`watcher = currentUser() AND resolution = Unresolved ORDER BY priority DESC, updated DESC`