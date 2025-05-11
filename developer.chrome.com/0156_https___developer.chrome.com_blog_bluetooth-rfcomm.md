---
url: https://developer.chrome.com/blog/bluetooth-rfcomm-updates-web-serial?hl=en
title: https://developer.chrome.com/blog/bluetooth-rfcomm-updates-web-serial?hl=en
date: 2025-05-11T16:54:03.765802
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/bluetooth-rfcomm-updates-web-serial?hl=en#main-content)


  * On this page


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Bluetooth RFCOMM updates in Web Serial 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


François Beaufort 
[ GitHub ](https://github.com/beaufortfrancois)
The [Web Serial API](https://developer.chrome.com/articles/serial) supports communicating with [RFCOMM services](https://developer.chrome.com/blog/serial-over-bluetooth#the_bluetooth_rfcomm_protocol) on paired Bluetooth Classic devices from Chrome 117 on desktop. For example, this allows wireless earbuds to use RFCOMM to manage audio settings and firmware updates. Check out [Serial over Bluetooth on the web](https://developer.chrome.com/blog/serial-over-bluetooth) to learn more.
From Chrome 130 for desktop, an improvement to the Web Serial API lets web apps detect when a Bluetooth RFCOMM serial port is available, without having to open the port. This prevents unnecessary reconnections when the wireless device was intentionally disconnected.
When a wireless device goes out of range of the host, any wireless serial port opened by a web app automatically closes. In such cases, the web app may attempt to reopen the port with the [SerialPort `open()`](https://developer.mozilla.org/docs/Web/API/SerialPort/open) method. However, if the wireless device was intentionally disconnected (for example, by the user from the operating system control panel), the web app should refrain from reopening the port to prevent reconnecting to the wireless device.
By exposing the logical connection state of the wireless device hosting the wireless serial port through a new boolean SerialPort `connected` attribute, web apps can now distinguish these cases, and only reconnect if the disconnection was unintentional.
The [SerialPort `connected`](https://wicg.github.io/serial/#dfn-connected) attribute is true for wireless serial ports if the wireless device hosting the port has any active connections to the system. For wired serial ports, it is true if the port is physically attached to the system.
The following snippet shows you how to check which devices are available and potentially connect to them automatically.
```
constports=awaitnavigator.serial.getPorts();
for(constportofports){
if(port.connected){
// Automatically try to connect to the Bluetooth device.
awaitport.open({baudRate:9600});
}else{
// Otherwise, when the port is not logically connected:
// 1. Prompt the user to make sure the Bluetooth device is available.
// 2. Show a "connect" button to try opening the port.
}
}

```

Previously, only wired serial ports dispatched [connect](https://developer.mozilla.org/docs/Web/API/SerialPort/connect_event) and [disconnect](https://developer.mozilla.org/docs/Web/API/SerialPort/disconnect_event) events. Bluetooth RFCOMM serial ports now dispatch these events when the port becomes logically connected or disconnected.
## Demo
SerialPort connected demo.
## Resources
  * [ChromeStatus entry](https://chromestatus.com/feature/5118102654418944)


## Acknowledgments
Thanks to Jack Hsieh and Reilly Grant for their reviews.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-09-16 UTC.

