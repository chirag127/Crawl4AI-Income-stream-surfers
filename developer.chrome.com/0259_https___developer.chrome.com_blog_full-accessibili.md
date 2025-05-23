---
url: https://developer.chrome.com/blog/full-accessibility-tree
title: https://developer.chrome.com/blog/full-accessibility-tree
date: 2025-05-11T16:56:14.440142
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/full-accessibility-tree#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/full-accessibility-tree?hl=es-419)




  * On this page
  * [What is the accessibility tree?](https://developer.chrome.com/blog/full-accessibility-tree#what_is_the_accessibility_tree)
  * [How is the tree created?](https://developer.chrome.com/blog/full-accessibility-tree#how_is_the_tree_created)
  * [Full accessibility tree in DevTools](https://developer.chrome.com/blog/full-accessibility-tree#full_accessibility_tree_in_devtools)
    * [Lazy tree construction](https://developer.chrome.com/blog/full-accessibility-tree#lazy_tree_construction)
  * [The tale of many trees](https://developer.chrome.com/blog/full-accessibility-tree#the_tale_of_many_trees)
    * [Multiple frames and site isolation](https://developer.chrome.com/blog/full-accessibility-tree#multiple_frames_and_site_isolation)
    * [Ignored and uninteresting nodes](https://developer.chrome.com/blog/full-accessibility-tree#ignored_and_uninteresting_nodes)
  * [Future ideas](https://developer.chrome.com/blog/full-accessibility-tree#future_ideas)
    * [Alternative filterings](https://developer.chrome.com/blog/full-accessibility-tree#alternative_filterings)
    * [Highlight a11y issues](https://developer.chrome.com/blog/full-accessibility-tree#highlight_a11y_issues)
    * [Surface accessibility actions in DevTools](https://developer.chrome.com/blog/full-accessibility-tree#surface_accessibility_actions_in_devtools)


  * [ Chrome for Developers ](https://developer.chrome.com/)


Was this helpful?
#  Full accessibility tree in Chrome DevTools 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [What is the accessibility tree?](https://developer.chrome.com/blog/full-accessibility-tree#what_is_the_accessibility_tree)
  * [How is the tree created?](https://developer.chrome.com/blog/full-accessibility-tree#how_is_the_tree_created)
  * [Full accessibility tree in DevTools](https://developer.chrome.com/blog/full-accessibility-tree#full_accessibility_tree_in_devtools)
    * [Lazy tree construction](https://developer.chrome.com/blog/full-accessibility-tree#lazy_tree_construction)
  * [The tale of many trees](https://developer.chrome.com/blog/full-accessibility-tree#the_tale_of_many_trees)
    * [Multiple frames and site isolation](https://developer.chrome.com/blog/full-accessibility-tree#multiple_frames_and_site_isolation)
    * [Ignored and uninteresting nodes](https://developer.chrome.com/blog/full-accessibility-tree#ignored_and_uninteresting_nodes)
  * [Future ideas](https://developer.chrome.com/blog/full-accessibility-tree#future_ideas)
    * [Alternative filterings](https://developer.chrome.com/blog/full-accessibility-tree#alternative_filterings)
    * [Highlight a11y issues](https://developer.chrome.com/blog/full-accessibility-tree#highlight_a11y_issues)
    * [Surface accessibility actions in DevTools](https://developer.chrome.com/blog/full-accessibility-tree#surface_accessibility_actions_in_devtools)


Johan Bay 
[ GitHub ](https://github.com/johanbay)
Chrome DevTools is launching a full accessibility tree making it easier for developers to get an overview of the whole tree. In this post find out how this tree is created and how to use it in your work.
## What is the accessibility tree?
Assistive technology such as screen readers use Chromium’s accessibility API to interact with web content. The underlying model of this API is the accessibility tree: **a tree of accessibility objects that assistive technology can query for attributes and properties and perform actions on**. Web developers shape and manipulate the accessibility tree primarily through DOM properties such as [ARIA attributes for HTML](https://www.w3.org/TR/html-aria/).
In [Chrome DevTools](https://developer.chrome.com/docs/devtools), we provide the accessibility pane to help developers understand how their content is exposed to assistive technology. Concretely, when a node is selected in the DOM tree viewer, the properties of the corresponding accessibility node displays in the pane together with a view of the node's ancestors and its immediate children.
## How is the tree created?
Before we get to what this new full tree view looks like in DevTools, let us briefly go over what the accessibility tree is in more tangible terms. The accessibility tree is a derivative of the DOM tree. Its structure is roughly the same, but simplified to remove nodes with no semantic content such as a `<div>` element purely used for styling. Each node in the tree has a role such as `Button` or `Heading`, and often a name that can be either from ARIA attributes or derived from the node’s contents. If we look at an HTML document:
```
<html>
<head>
 <title>How old are you?</title>
</head>
<body>
 <label for="age">Age</label>
 <input id="age" type="number" name="age" value="42">
 <div>
  <button>Back</button>
  <button>Next</button>
 </div>
</body>
</html>

```

The renderer in Chromium, named Blink, derives an internal accessibility tree roughly as follows.
```
role='rootWebArea' focusable name='How old are you?'
 role='genericContainer' ignored
  role='genericContainer' ignored
   role='labelText'
    role='staticText' name='Age'
   role='spinButton' editable focusable name='Age' value='42'
    role='genericContainer' editable
     role='staticText' editable name='42'
   role='genericContainer'
    role='button' focusable name='Back'
     role='staticText' name='Back'
    role='button' focusable name='Next'
     role='staticText' name='Next'

```

Note that this representation contains multiple superfluous nodes with role `genericContainer`, which seemingly contradicts the statement above that the accessibility tree is a simplified derivative of the DOM tree. Still, most of these nodes only occur in the internal tree and would not be exposed to assistive technology. Since DevTools collects its accessibility information directly from the renderer process, this is the tree representation that DevTools handles.
## Full accessibility tree in DevTools
The new, full accessibility tree synchronized with the DOM tree so developers can switch back and forth between the two trees. We hope that the new tree will prove more explorable, useful, and easier to use.
Now that you know how the accessibility tree works, you can use DevTools to see how the new tree view looks. The following HTML document with a title, heading, and two buttons is used to show the tree.
```
<!DOCTYPE html>
<title>Test</title>
<h1>Heading for example page</h1>
<div>
 <button>Back</button>
 <button>Next</button>
</div>

```

The previous tree view would only enable you to explore a single node and its ancestors.
Now, when you toggle the new tree, it replaces the DOM tree view and allows you to see the full accessibility tree for the page:
### Lazy tree construction
To make the tree performant even for larger sites, the tree is lazily constructed on the frontend as it is explored. Once a node is expanded in the tree, the children for the nodes are fetched through Chrome DevTools Protocol (CDP) and the tree is rebuilt.
### Live
The new tree view is live and dynamically updates if the accessibility tree changes in the renderer. It hooks into the same mechanics that would notify assistive technology of changes to the tree, and uses that to emit events to the DevTools frontend with updated nodes. In practice, the CDP backend listens for updates to the tree, keeps track of which nodes have been requested before, and sends events to the DevTools frontend if any of these nodes changes.
## The tale of many trees
In the description of [what the accessibility tree is](https://developer.chrome.com/blog/full-accessibility-tree#what_is_the_accessibility_tree) you learned how Blink constructs an accessibility tree for the DOM it is rendering, and DevTools fetches this tree through CDP. While this is true, we left out some complications in this description. In reality, there are quite a lot of [different ways to experience](https://en.wikipedia.org/wiki/Blind_men_and_an_elephant) the accessibility tree in Chromium. When designing the new tree view for DevTools, we have made some choices along the way about what part of Chromium’s accessibility internals we wanted to surface.
### Platforms
Every platform has a different accessibility API and while the shape of the tree is the same across all platforms, the API for interacting with the tree is different, and the names of attributes can differ. DevTools shows Chromium’s internal tree where roles and attributes tend to match those defined in the [ARIA](https://www.w3.org/TR/wai-aria-1.1/) specification.
### Multiple frames and site isolation
Since Chromium not only puts the content of every tab in different renderer processes but also [isolates cross-site documents in different renderer processes](https://www.chromium.org/developers/design-documents/site-isolation), we have to connect to each out-of-process child document separately over CDP and fetch its accessibility tree. We then stitch these subtrees together on the frontend to give the illusion of one coherent tree, although they live in different renderer processes in Chromium.
### Ignored and uninteresting nodes
We hide some nodes per default: ignored nodes, and nodes with role “generic” with no name. These nodes carry no semantic meaning and, in the case of ignored nodes, are not exposed to assistive technology. We hide these nodes to avoid cluttering the tree view. If we did not, the accessibility tree for most web pages would instead look something like this:
The caveat here is that this essentially means that we need to construct yet another tree than what is available on the backend. Say, for example, that we have nodes A, B, C, and X where A has child X and B, and X has child C. If X is an ignored node, we prune X from the tree and instead create a tree where C is a child to A.
On the frontend, we construct the full tree including ignored nodes and only prune them just before rendering the nodes. We do this for two reasons:
  * **It makes it much simpler to handle node updates from the backend** , since we have the same tree structure on both endpoints. For example, if the node B is removed in the example, we would receive an update for node X (since its children have changed), but if we had pruned that node we would struggle to figure out what to update.
  * **It ensures that all DOM nodes have a corresponding accessibility node.** When the tree is toggled, we select the node corresponding to the node currently selected in the DOM tree. So for the previous example, if the user toggles the tree while the DOM node corresponding to X is selected, we inject X between the nodes A and B and select X in the tree. This allows the user to inspect the accessibility node for all DOM nodes and help determine why the node is ignored.


## Future ideas
Launching the new accessibility tree is just the start. We have a few ideas for future projects we could build on top of the new view, but we are also eager to [hear your feedback](https://goo.gle/devtools-a11y-tree-feedback)!
### Alternative filterings
As explained above, we currently filter out nodes that are deemed uninteresting. We could provide a way to disable this behavior and show all nodes, or provide alternative filterings such as **Show landmark nodes** or **Show headings**.
### Highlight a11y issues
We could incorporate an “accessibility best practice” analysis with the tree and highlight accessibility issues directly on the offending nodes.
### Surface accessibility actions in DevTools
The tree we currently show is purely one-way: It allows us to get an idea of what information would be fed to assistive technology when browsing a specific webpage. Accessibility actions represent the communication in the other direction: They allow assistive technology to act on the presented UI. We could surface such actions in DevTools to allow actions such as “clicking”, scrolling, or changing values on the page using the API available to assistive technology.
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2021-12-13 UTC.

