---
url: https://developer.chrome.com/blog/devtools-annotations?hl=en
title: https://developer.chrome.com/blog/devtools-annotations?hl=en
date: 2025-05-11T16:55:11.159067
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/devtools-annotations?hl=en#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/devtools-annotations?hl=es-419)




  * On this page
  * [Annotated time ranges](https://developer.chrome.com/blog/devtools-annotations?hl=en#annotated_time_ranges)
  * [Annotated entries](https://developer.chrome.com/blog/devtools-annotations?hl=en#annotated_entries)
  * [Entry connections](https://developer.chrome.com/blog/devtools-annotations?hl=en#entry_connections)
  * [Delete and hide annotations](https://developer.chrome.com/blog/devtools-annotations?hl=en#delete_and_hide_annotations)
  * [Save or load annotated traces](https://developer.chrome.com/blog/devtools-annotations?hl=en#save_or_load_annotated_traces)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Annotate traces directly in the Performance panel 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Annotated time ranges](https://developer.chrome.com/blog/devtools-annotations?hl=en#annotated_time_ranges)
  * [Annotated entries](https://developer.chrome.com/blog/devtools-annotations?hl=en#annotated_entries)
  * [Entry connections](https://developer.chrome.com/blog/devtools-annotations?hl=en#entry_connections)
  * [Delete and hide annotations](https://developer.chrome.com/blog/devtools-annotations?hl=en#delete_and_hide_annotations)
  * [Save or load annotated traces](https://developer.chrome.com/blog/devtools-annotations?hl=en#save_or_load_annotated_traces)


Alina Varkki 
[ GitHub ](https://github.com/AlinaVarkki) [ LinkedIn ](https://www.linkedin.com/in/alina-varkki-2598a116b)
Published: November 13, 2024 
Imagine looking at a performance trace and wanting to highlight a specific area, like the longest task or an unnecessary chunk of work. Perhaps you wanted to make notes for future reference or share your findings with a colleague. What's the best way to do that?
Of course, it's printing out the trace on a huge piece of paper and manually drawing and writing your notes, or using third-party software to draw notes on a screenshot of a trace! (Though that was the best way until now.)
Annotating a trace by hand ([Ori Livneh](https://commons.wikimedia.org/wiki/File:Scrutinizing_VisualEditor_performance_timeline.png), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0), Wikimedia Commons)
As part of our team's dedication to [streamlining developer workflows](https://developer.chrome.com/blog/perf-tooling-2024), we are excited to introduce an alternative to those options: the ability to add annotations directly to the trace within the **Performance** panel!
Now, you can annotate traces in place, navigate those annotations with ease, and even save them directly within the trace file. This makes sharing highlighted insights as straightforward as sending a file, while eliminating the need for external tools or workarounds. Annotations can not only help you with debugging performance, but also help to quickly get on the same page with your colleague, or uplevel their understanding of what's going on without much back and forth.
Exploring annotations in the Performance panel
There are three types of annotations:
  1. **Annotated time ranges** : Labeling any time range in the timeline
  2. **Annotated entries** : Adding a label to any entry in the timeline
  3. **Entry connections** : Connecting any two entries with an arrow to show their relation


Let's look at each type of annotation and the scenarios you might find yourself in when they come in handy.
## Annotated time ranges
A common workflow in DevTools is recording a trace to debug a slow interaction. The trace view can seem overwhelming at first, but as you drill down on specific event handlers and call stacks, it'll start to make sense. One thing you can do to make the trace view easier to work with is create an annotation to label how a block of time is generally spent. So for example, it might be helpful to annotate the _time range_ for the UI to meaningfully update after a user interaction.
Annotating the time range from the start of an interaction to the time the UI is updated
**To annotate a time range** : Hold `Shift` and drag from the start of the interaction to the UI update. Afterwards, type a label to create the annotation. If the selected range is not correct, cancel it by clicking away before typing. Or, to edit an annotation's label, double-click on it. At this time you cannot adjust the time range of an existing annotation. If the timeframe is incorrect, delete the annotation and create a new one.
With this annotation, you'll have a clearer look at all the work that has to happen before the user-visible change, so you can focus your debugging accordingly.
## Annotated entries
To make the user-visible change more obvious, you can also annotate the task responsible for the transition with an _entry label_.
Annotating entries in the Performance panel
**To create a label for the entry** : Double-click on the selected entry and type your label or right-click on the entry and select "Label Entry" from the context menu. To edit an annotation's label, double-click on the entry or the label. Alternatively, select the "Label Entry" option from the context menu.
With these entry annotations, it's easier to spot the work that is (or is not) critical to the interaction and how much time it takes.
## Entry connections
The third way we can annotate the trace is to draw the _connection_ between the interaction and the long task responsible for the transition.
Annotating entry connections in the Performance panel
**To create a connection between entries** : Double-click on the entry that you want to connect to another one and click the arrow that appears on the right of that entry. Next, click the entry you would like to connect it to. Alternatively, right-click on the entry and select "Link Entries" from the entry context menu.
So even though the interaction itself had ended, you can use this type of annotation to more clearly show how it's connected to the subsequent long tasks that ultimately block the UI.
## Delete and hide annotations
All annotations can be deleted quickly from the annotations list view in the sidebar. Hovering over an annotation reveals a bin icon delete. Click this icon to delete the annotation.
Deleting an annotation in the Performance panel
Alternatively, to delete entry labels and entries connection annotations associated with a specific event, right-click on the event and select "Delete annotations". Annotations with labels can also be deleted by removing the label and saving the annotations.
If you want to hide annotations without deleting them so they don't disturb you from exploring the trace, just check the "hide annotations" checkbox located at the bottom of the annotations sidebar. This preference will be saved. When you load a trace with annotations while this setting is enabled, the annotations will remain hidden until you clear the checkbox.
## Save or load annotated traces
Great, you added all those annotations to help yourself and others to make sense of the trace. What's next?
There's no need for taking screenshots of the trace to send them to a colleague like in the old times, before annotations. Just save your annotated file and send them that file. That's it—they can upload the file into the **Performance** panel and see all of the annotations you made in the context of the trace, or maybe even add more annotations and send them back to you!
Saving a trace with or without annotations in the Performance panel
DevTools will also save other kinds of [customizations](https://developer.chrome.com/blog/devtools-customization) in the trace view. For example, you can isolate an area of interest by zooming in and setting a breadcrumb, or hide entries in irrelevant call stacks, and all of those settings will be persisted by the trace file, making it even easier to collaborate on performance debugging. With all of these customizations, you can call attention to what matters most while providing the context of the whole, interactive trace—unlike a screenshot.
To preserve annotations and other customizations, click the **Save trace** option under the download icon download. When a trace is loaded, it will contain all of those customizations. Saving with annotations is the default option, but if you'd like to only save the raw trace file, select the **Save trace without annotations** option.
## Conclusion
This may seem like a lot of information to absorb, but don't worry! Instructions for creating annotations can always be found in the annotations tab of the **Performance** panel sidebar. This tab provides instructions when no annotations exist, and displays a list view of annotations once they are created.
Instructions for working with annotations in the Performance panel sidebar
Just like that, annotations in the **Performance** panel empower developers to pinpoint crucial moments within a trace, adding personalized context and insights. This streamlines the analysis process, making it easier to share and collaborate on performance optimizations. Try out the annotations in the Performance panel and let us know what you think. If you have any feedback, we'd love to read your comments in the [public issue](https://crbug.com/329541444).
Say goodbye to the need for external tools and hello to a more efficient workflow!
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-11-13 UTC.

