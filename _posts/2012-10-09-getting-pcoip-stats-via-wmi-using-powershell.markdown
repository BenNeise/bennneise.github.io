---
layout: post
title: Getting PCOIP statistics via WMI using PowerShell
date: '2012-10-09 11:30:20'
tags: vmware-horizon-view powershell
---

I was at a training course last week and  it was mentioned briefly on one of the slides that PCOIP session statistics were available via WMI. After a quick Google, I found [MyVirtualCloud's page](http://myvirtualcloud.net/?p=2069), which details the class, and property names.

The following is a PowerShell function, which pulls this information from WMI, appends the names and descriptions, and returns an object. You could, for example, export the returned object to an HTML page. Or use the function against a range of machines to look for outliers.

```powershell
function Get-PCOIPStatsViaWMI($objComputerName = (Throw "Please use with a computer name")){
    $arrResults = @()
    $objWMIPCoIPSessionGeneralStatistics = Get-WMIObject -Class Win32_PerfRawData_TeradiciPerf_PCoIPSessionGeneralStatistics -ComputerName $objComputerName
    $objSessionDurationSeconds = New-Object PSObject $objSessionDurationSeconds | Add-Member -Name "Name" -MemberType NoteProperty -Value "Session Duration Seconds"
    $objSessionDurationSeconds | Add-Member -Name "Description" -MemberType NoteProperty -Value "An incrementing number that represents the total number of seconds the PCoIP session has been open."
    $objSessionDurationSeconds | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionGeneralStatistics.SessionDurationSeconds
    $arrResults += $objSessionDurationSeconds
    $objBytesReceived = New-Object PSObject
    $objBytesReceived | Add-Member -Name "Name" -MemberType NoteProperty -Value "Bytes Received"
    $objBytesReceived | Add-Member -Name "Description" -MemberType NoteProperty -Value "Total number of bytes that have been received since the PCoIP session started."
    $objBytesReceived | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionGeneralStatistics.BytesReceived
    $arrResults += $objBytesReceived
    $objBytesSent = New-Object PSObject
    $objBytesSent | Add-Member -Name "Name" -MemberType NoteProperty -Value "Bytes Sent"
    $objBytesSent | Add-Member -Name "Description" -MemberType NoteProperty -Value "Total number of bytes that have been transmitted since the PCoIP session started."
    $objBytesSent | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionGeneralStatistics.BytesSent
    $arrResults += $objBytesSent
    $objPacketsReceived = New-Object PSObject 
    $objPacketsReceived | Add-Member -Name "Name" -MemberType NoteProperty -Value "Packets Received" 
    $objPacketsReceived | Add-Member -Name "Description" -MemberType NoteProperty -Value "Total number of packets that have been received since the PCoIP session started. Note that not all packets are the same size." 
    $objPacketsReceived | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionGeneralStatistics.PacketsReceived 
    $arrResults += $objPacketsReceived 
    $objPacketsSent = New-Object PSObject 
    $objPacketsSent | Add-Member -Name "Name" -MemberType NoteProperty -Value "Packets Sent" 
    $objPacketsSent | Add-Member -Name "Description" -MemberType NoteProperty -Value "Total number of packets that have been transmitted since the PCoIP session started. Note that not all packets are the same size." 
    $objPacketsSent | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionGeneralStatistics.PacketsSent 
    $arrResults += $objPacketsSent 
    $objRXPacketsLost = New-Object PSObject
    $objRXPacketsLost | Add-Member -Name "Name" -MemberType NoteProperty -Value "RX Packets Lost"
    $objRXPacketsLost | Add-Member -Name "Description" -MemberType NoteProperty -Value "Total number of receive packets that have been lost since the PCoIP session started."
    $objRXPacketsLost | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionGeneralStatistics.RXPacketsLost
    $arrResults += $objRXPacketsLost
    $objTXPacketsLost = New-Object PSObject 
    $objTXPacketsLost | Add-Member -Name "Name" -MemberType NoteProperty -Value "TX Packets Lost"
    $objTXPacketsLost | Add-Member -Name "Description" -MemberType NoteProperty -Value "Total number of transmit packets that have been lost since the PCoIP session started."
    $objTXPacketsLost | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionGeneralStatistics.TXPacketsLost
    $arrResults += $objTXPacketsLost 
    # PCOIP Session Network Statistics 
    $objWMIPCoIPSessionNetworkStatistics = Get-WMIObject -Class Win32_PerfRawData_TeradiciPerf_PCoIPSessionNetworkStatistics -ComputerName $objComputerName
    $objRoundTripLatencyms = New-Object PSObject
    $objRoundTripLatencyms | Add-Member -Name "Name" -MemberType NoteProperty -Value "Round Trip Latency ms" 
    $objRoundTripLatencyms | Add-Member -Name "Description" -MemberType NoteProperty -Value "Round trip latency (in milliseconds) between server and client." 
    $objRoundTripLatencyms | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionNetworkStatistics.RoundTripLatencyms 
    $arrResults += $objRoundTripLatencyms
    $objRXBWPeakkbitPersec = New-Object PSObject
    $objRXBWPeakkbitPersec | Add-Member -Name "Name" -MemberType NoteProperty -Value "RX BW Peak kbit/sec"
    $objRXBWPeakkbitPersec | Add-Member -Name "Description" -MemberType NoteProperty -Value "Peak bandwidth for incoming PCoIP packets within a one second sampling period."
    $objRXBWPeakkbitPersec | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionNetworkStatistics.RXBWPeakkbitPersec 
    $arrResults += $objRXBWPeakkbitPersec 
    $objTXBWActiveLimitkbitPersec = New-Object PSObject 
    $objTXBWActiveLimitkbitPersec | Add-Member -Name "Name" -MemberType NoteProperty -Value "TX BW Active Limit kbit/sec"
    $objTXBWActiveLimitkbitPersec | Add-Member -Name "Description" -MemberType NoteProperty -Value "The current estimate of the available network bandwidth, updated every second."
    $objTXBWActiveLimitkbitPersec | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionNetworkStatistics.TXBWActiveLimitkbitPersec 
    $arrResults += $objTXBWActiveLimitkbitPersec 
    # PCOIP Session Audio Statistics 
    $objWMIPCoIPPCoIPSessionAudioStatistics = Get-WMIObject -Class Win32_PerfRawData_TeradiciPerf_PCoIPSessionAudioStatistics -ComputerName $objComputerName
    $objAudioBytesReceived = New-Object PSObject
    $objAudioBytesReceived | Add-Member -Name "Name" -MemberType NoteProperty -Value "Audio Bytes Received" 
    $objAudioBytesReceived | Add-Member -Name "Description" -MemberType NoteProperty -Value "Total number of audio bytes that have been received since the PCoIP session started."
    $objAudioBytesReceived | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPPCoIPSessionAudioStatistics.AudioBytesReceived
    $arrResults += $objAudioBytesReceived
    $objAudioBytesSent = New-Object PSObject 
    $objAudioBytesSent | Add-Member -Name "Name" -MemberType NoteProperty -Value "Audio Bytes Sent"
    $objAudioBytesSent | Add-Member -Name "Description" -MemberType NoteProperty -Value "Total number of audio bytes that have been sent since the PCoIP session started."
    $objAudioBytesSent | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPPCoIPSessionAudioStatistics.AudioBytesSent 
    $arrResults += $objAudioBytesSent 
    $objAudioTXBWLimitkbitPersec = New-Object PSObject 
    $objAudioTXBWLimitkbitPersec | Add-Member -Name "Name" -MemberType NoteProperty -Value "Audio TX BW Limit kbit/sec" 
    $objAudioTXBWLimitkbitPersec | Add-Member -Name "Description" -MemberType NoteProperty -Value "Transmit bandwidth limit for outgoing audio packets as defined by the GPO setting." 
    $objAudioTXBWLimitkbitPersec | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPPCoIPSessionAudioStatistics.AudioTXBWLimitkbitPersec 
    $arrResults += $objAudioTXBWLimitkbitPersec 
    # PCOIP Session Imaging Statistics 
    $objWMIPCoIPSessionImagingStatistics = Get-WMIObject -Class Win32_PerfRawData_TeradiciPerf_PCoIPSessionImagingStatistics -ComputerName $objComputerName 
    $objImagingBytesReceived = New-Object PSObject
    $objImagingBytesReceived | Add-Member -Name "Name" -MemberType NoteProperty -Value "Imaging Bytes Received"
    $objImagingBytesReceived | Add-Member -Name "Description" -MemberType NoteProperty -Value "Total number of imaging bytes that have been received since the PCoIP session started."
    $objImagingBytesReceived | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionImagingStatistics.ImagingBytesReceived
    $arrResults += $objImagingBytesReceived 
    $objImagingBytesSent = New-Object PSObject $objImagingBytesSent | Add-Member -Name "Name" -MemberType NoteProperty -Value "Imaging Bytes Sent" 
    $objImagingBytesSent | Add-Member -Name "Description" -MemberType NoteProperty -Value "Total number of imaging bytes that have been sent since the PCoIP session started."
    $objImagingBytesSent | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionImagingStatistics.ImagingBytesSent 
    $arrResults += $objImagingBytesSent 
    $objImagingEncodedFramesPersec = New-Object PSObject 
    $objImagingEncodedFramesPersec | Add-Member -Name "Name" -MemberType NoteProperty -Value "Imaging Encoded Frames/sec" 
    $objImagingEncodedFramesPersec | Add-Member -Name "Description" -MemberType NoteProperty -Value "The number of imaging frames which were encoded over a one second sampling period."
    $objImagingEncodedFramesPersec | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionImagingStatistics.ImagingEncodedFramesPersec 
    $arrResults += $objImagingEncodedFramesPersec
    $objImagingActiveMinimumQuality = New-Object PSObject 
    $objImagingActiveMinimumQuality | Add-Member -Name "Name" -MemberType NoteProperty -Value "Imaging Active Minimum Quality" 
    $objImagingActiveMinimumQuality | Add-Member -Name "Description" -MemberType NoteProperty -Value "The lowest encoded quality (0 to 100), updated every second. Not to be confused with the GPO setting." 
    $objImagingActiveMinimumQuality | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionImagingStatistics.ImagingActiveMinimumQuality 
    $arrResults += $objImagingActiveMinimumQuality
    $objImagingDecoderCapabilitykbitPersec = New-Object PSObject
    $objImagingDecoderCapabilitykbitPersec | Add-Member -Name "Name" -MemberType NoteProperty -Value "Imaging Decoder Capability kbit/sec"
    $objImagingDecoderCapabilitykbitPersec | Add-Member -Name "Description" -MemberType NoteProperty -Value "The current estimate of the decoder processing capability."
    $objImagingDecoderCapabilitykbitPersec | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionImagingStatistics.ImagingDecoderCapabilitykbitPersec 
    $arrResults += $objImagingDecoderCapabilitykbitPersec 
    # PCOIP Session USB Statistics 
    $objWMIPCoIPSessionUSBStatistics = Get-WMIObject -Class Win32_PerfRawData_TeradiciPerf_PCoIPSessionUSBStatistics -ComputerName $objComputerName 
    # Note: The following USB session statistics are only available for the Zero Client to Soft Host configuration. # These values will be 0 for the Thin (Soft) Client to Soft Host configuration. 
    $objUSBBytesReceived = New-Object PSObject 
    $objUSBBytesReceived | Add-Member -Name "Name" -MemberType NoteProperty -Value "USB Bytes Received" 
    $objUSBBytesReceived | Add-Member -Name "Description" -MemberType NoteProperty -Value "Total number of USB bytes that have been received since the PCoIP session started." 
    $objUSBBytesReceived | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionUSBStatistics.USBBytesReceived 
    $arrResults += $objUSBBytesReceived
    $objUSBBytesSent = New-Object PSObject 
    $objUSBBytesSent | Add-Member -Name "Name" -MemberType NoteProperty -Value "USB Bytes Sent" 
    $objUSBBytesSent | Add-Member -Name "Description" -MemberType NoteProperty -Value "Total number of USB bytes that have been sent since the PCoIP session started." 
    $objUSBBytesSent | Add-Member -Name "Value" -MemberType NoteProperty -Value $objWMIPCoIPSessionUSBStatistics.USBBytesSent 
    $arrResults += $objUSBBytesSent
    Return $arrResults
}
```

Use like so

`Get-PCOIPStatsViaWMI("Computer01")`

It's not the most elegant script I've ever written. If I get the time, I think I'll try and streamline it; and maybe add some "expected ranges". I may also export  a timestamped XML object, this would allow comparisons over a time-range (which will allow bandwidth calculations).

[MindFlux's PCOIP log viewer](http://mindfluxinc.net/?p=195) is still a better solution for investigating problems on a single machine, but this might help get an overview of PCOIP performance across the whole estate.


