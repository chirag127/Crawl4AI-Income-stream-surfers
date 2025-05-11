---
url: https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en
title: https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en
date: 2025-05-11T16:56:35.207384
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#main-content)
Sign in


  * On this page
  * [Programming experience](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#programming_experience)
  * [Included hardware](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#included_hardware)
  * [Supported applications](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#supported_applications)
  * [Connect to the SPIKE Hub](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#connect_to_the_spike_hub)
    * [Web Bluetooth API connection](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#web_bluetooth_api_connection)
    * [Web Serial API connection](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#web_serial_api_connection)
  * [Reasons to go web-first and use web hardware APIs](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#reasons_to_go_web-first_and_use_web_hardware_apis)
  * [Tinker with LEGO on the web](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#tinker_with_lego_on_the_web)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  How LEGO® Education uses the Web Bluetooth and the Web Serial APIs 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Programming experience](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#programming_experience)
  * [Included hardware](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#included_hardware)
  * [Supported applications](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#supported_applications)
  * [Connect to the SPIKE Hub](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#connect_to_the_spike_hub)
    * [Web Bluetooth API connection](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#web_bluetooth_api_connection)
    * [Web Serial API connection](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#web_serial_api_connection)
  * [Reasons to go web-first and use web hardware APIs](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#reasons_to_go_web-first_and_use_web_hardware_apis)
  * [Tinker with LEGO on the web](https://developer.chrome.com/blog/lego-education-spike-web-bluetooth-web-serial?hl=en#tinker_with_lego_on_the_web)


Thomas Steiner 
[ GitHub ](https://github.com/tomayac) [ Glitch ](https://glitch.com/@tomayac) [ LinkedIn ](https://www.linkedin.com/in/thomassteinerlinkedin) [ Mastodon ](https://toot.cafe/@tomayac) [ Bluesky ](https://bsky.app/profile/tomayac.com) [ Homepage ](https://blog.tomayac.com/)
Jakob Dam Jensen 
[ LinkedIn ](https://www.linkedin.com/in/jakobdamjensen)
The [LEGO® Education SPIKE™ Prime Set](https://education.lego.com/products/lego-education-spike-prime-set/45678#spike%E2%84%A2-prime) is a STEAM (science, technology, engineering, arts and mathematics) learning tool for students in grades six through eight (about 11 to 13 years).
Combining colorful LEGO building elements, easy-to-use hardware, and an intuitive drag-and-drop coding language based on [Scratch](https://scratch.mit.edu/) and Python, SPIKE Prime continuously engages students through playful learning activities to think critically and solve complex problems, regardless of their learning level… while having fun!
## Programming experience
Students use either icon blocks, word blocks (default), or Python code to program their models. The programming environment is adapted from the [Scratch editor](https://scratch.mit.edu/projects/editor/?tutorial=getStarted), familiar to many students already from early STEAM education in school.
In the two visual modes, students connect blocks by dragging and dropping them onto the programming canvas. They hook up the various blocks by connecting them.
More advanced students can opt to use real Python code directly, which comes with an integrated knowledge base to support students while they code.
Once they've created a program in the LEGO Education SPIKE app, the students send the program to the LEGO Education Spike Prime hub over a Bluetooth or USB connection. The hub executes the program and controls the LEGO model.
## Included hardware
The brain of the SPIKE Education kit is the hub, which serves to control the various other pieces of hardware like the sensors and the motors. The kit includes a color sensor, distance sensor, and force sensor. There are also two motors: one large, one medium. The hub connects to the computer with Bluetooth or USB.
The large hub, three sensors for color, distance, and force, and two motors.
## Supported applications
Apart from [platform-specific apps](https://education.lego.com/teacher-resources/lego-education-spike-prime/support-technical-info/lego-education-spike-prime-support-technical-info-get-the-lego-education-spiketm-app), LEGO also offers the SPIKE web app, which is accessible at [spike.legoeducation.com](https://spike.legoeducation.com). The app is not cached in the browser, so users always need to be connected to the Internet for the web app to work.
LEGO officially supports Chrome browsers on Windows 10 and 11, MacBooks, and Chromebooks. Caching improvements and making the app installable are planned features for the future.
## Connect to the SPIKE Hub
The SPIKE Prime hub and the SPIKE Essential hub can be connected to the computer using Bluetooth or USB. By default, the web app uses Bluetooth with the [Web Bluetooth API](https://developer.chrome.com/docs/capabilities/bluetooth).
Alternatively, the web app uses the [Web Serial API](https://developer.chrome.com/docs/capabilities/serial) when connected with USB. In both cases, apart from the USB cable, the connection flow is almost identical.
Once connected, students upload their programs to one of the 20 storage slots of the large hub.
For communicating with the hub, the Web Bluetooth and the Web Serial API need a [`BluetoothDevice`](https://developer.mozilla.org/docs/Web/API/BluetoothDevice) or a [`SerialPort`](https://developer.mozilla.org/docs/Web/API/SerialPort) respectively. These are obtained in the code snippets taken from the live app.
### Web Bluetooth API connection
```
(X.next=4),
navigator.bluetooth.requestDevice({
filters:[
{
namePrefix:'GDX',
},
],
optionalServices:['d91714ef-28b9-4f91-ba16-f0d9a604f112'],
});

```

### Web Serial API connection
```
constv=yieldnavigator.serial.requestPort({
filters:[{
usbVendorId:Zt.SerialVendorId.LEGO// 1684
}]
});
yieldv.open({
baudRate:115200
});

```

## Reasons to go web-first and use web hardware APIs
Currently, LEGO maintains [independent versions](https://education.lego.com/downloads/spike-app/software) of their app for Android, macOS/iPadOS, and Windows; plus [legacy versions](https://education.lego.com/downloads/spike-legacy-app/software) of the platform-specific apps on top, in addition to the web app. By pushing the web app on platforms that support the underlying web hardware APIs in Chrome, namely macOS, Windows, and ChromeOS, LEGO developers can reduce their app maintenance burden significantly.
Another reason is download size. The web app downloads less than 20 MB in total, whereas the macOS and iPadOS app weighs 115 MB, the Android app 178 MB, and the Windows app clocks in at 292 MB. The initial install however, does not include the lesson material needed in classrooms. After downloading this material, the size increases by almost 1 GB. On the web app, the lesson content is streamed, which enables the user to always have the latest version and only download the exact lesson they are looking at.
Apart from these technical reasons, simplicity of classroom use is another strong argument to go web-first. Students don't need to install an app and keep it updated. Instead, they just follow a link and always work with the most recent version. From LEGO's end, content updates are always possible, independent from app store review processes.
## Tinker with LEGO on the web
LEGO was always about creatively assembling bricks, and with LEGO Education SPIKE being accessible from web browsers, this kit is no exception from the rule.
The developer community has already begun to create code that talks to SPIKE. For example, [PyREPL-JS](https://github.com/tuftsceeo/PyREPLforSPIKE) was started by [Gabriel Sessions](https://github.com/gabrielsessions) at Tufts University. PyREPL-JS provides a [MicroPython REPL](https://pyrepl.web.app/) (read–eval–print loop) for web pages to talk to the SPIKE hub. [Ethan Danahy](https://github.com/edanahy), also from Tufts, then uses this REPL for a number of [Web-Interfaces for SPIKE Prime](https://edanahy.github.io/WebSPIKE/), one of which is the [breakdancer synced to an audio file](https://education.lego.com/lessons/prime-life-hacks/break-dance#coding-tips).
The university hosted a workshop on doing [Machine Learning with SPIKE](https://edanahy.github.io/MLwithSPIKEworkshop/) and hosts a [Robotics Playground](https://www.ceeoinnovations.org/RoboticsPlayground/) with instructions and code samples. A good place to start is [Hello SPIKE](https://edanahy.github.io/HelloSPIKE/).
By allowing students to communicate with physical LEGO models from within the browser, the Web Serial and Web Bluetooth APIs open up a world of possibilities for educational, creative, and entertainment applications. Students will always have the latest version of the app without needing to update it.
LEGO developers in the long run will have fewer apps to maintain, which means reduced cost and less development effort, leaving more time for doing what LEGO is best known for: unlocking creativity.
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2023-05-22 UTC.

