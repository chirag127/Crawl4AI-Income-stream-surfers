---
url: https://developer.chrome.com/blog/command-and-commandfor?hl=en
title: https://developer.chrome.com/blog/command-and-commandfor?hl=en
date: 2025-05-11T16:54:35.687814
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/command-and-commandfor?hl=en#main-content)
Sign in


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Introducing command and commandfor 
Stay organized with collections  Save and categorize content based on your preferences. 
Keith Cirkel 
[ GitHub ](https://github.com/keithamus) [ Mastodon ](https://indieweb.social/@keithamus) [ Bluesky ](https://bsky.app/profile/keithamus.social)
Published: March 7, 2025 
Buttons are essential to making dynamic web applications. Buttons open menus, toggle actions, and submit forms. They provide the foundation of interactivity on the web. Making buttons simple and accessible can lead to some surprising challenges. Developers building micro-frontends or component systems can encounter solutions that become more complex than necessary. While frameworks help, the web can do more here.
Chrome 135 introduces new capabilities for providing declarative behaviour with the new `command` and `commandfor` attributes, enhancing and replacing the `popovertargetaction` and `popovertarget` attributes. These new attributes can be added to buttons, letting the browser address some core issues around simplicity and accessibility, and provide built-in common functionality.
## Traditional patterns
Building button behaviours without a framework can pose some interesting challenges as production code evolves. While HTML offers `onclick` handlers to buttons, these are often disallowed outside of demos or tutorials due to Content Security Policy (CSP) rules. While these events are dispatched on button elements, buttons are usually placed on a page to control _other_ elements requiring code to control two elements at once. You also need to ensure this interaction is accessible to users of assistive technology. This often leads to code looking a bit like this:
```
<div class="menu-wrapper">
 <button class="menu-opener" aria-expanded="false">
  Open Menu
 </button>
 <div popover class="menu-content">
  <!-- ... -->
 </div>
</div>
<script type="module">
document.addEventListener('click', e => { 
 const button = e.target;
 if (button.matches('.menu-opener')) {
  const menu = button
   .closest('.menu-wrapper')
   .querySelector('.menu-content');
  if (menu) {
   button.setAttribute('aria-expanded', 'true');
   menu.showPopover();
   menu.addEventListener('toggle', e => {
    // reset back to aria-expanded=false on close
    if (e.newState == 'closed') {
     button.setAttribute('aria-expanded', 'false');
    }
   }, {once: true})
  }
 }
});
</script>

```

This approach can be a little brittle, and frameworks aim to improve ergonomics. A common pattern with a framework like React might involve mapping the click to a state change:
```
functionMyMenu({children}){
const[isOpen,setIsOpen]=useState(false);
constopen=useCallback(()=>setIsOpen(true),[]);
consthandleToggle=useCallback((e)=>{
// popovers have light dismiss which influences our state
setIsOpen(e.newState==='open')
},[]);
constpopoverRef=useRef(null);
useEffect(()=>{
if(popoverRef.current){
if(isOpen){
popoverRef.current.showPopover();
}else{
popoverRef.current.hidePopover();
}
}
},[popoverRef,isOpen]);
return(
<>
<buttononClick={open}aria-expanded={isOpen}>
OpenMenu
</button>
<divpopoveronToggle={handleToggle}ref={popoverRef}>
{children}
</div>
</>
);
}

```

Many other frameworks also aim to provide similar ergonomics, for example this might be written in AlpineJS as:
```
<div x-data="{open: false}">
 <button @click="open = !open; $refs.popover.showPopover()" :aria-expanded="open">
  Open Menu
 </button>
 <div popover x-ref="popover" @toggle="open = $event.newState === 'open'">
  <!-- ... -->
 </div>
</div>

```

While writing this in Svelte might look something like:
```
<script>
letpopover;
letopen=false;
functiontogglePopover(){
open?popover.hidePopover():popover.showPopover();
open=!open;
}
</script>
<buttonon:click={togglePopover}aria-expanded={open}>
OpenMenu
</button>
<divbind:this={popover}popover>
<!--...-->
</div>

```

Some design systems or libraries might go a step further, by providing wrappers around button elements that encapsulate the state changes. This abstracts state changes behind a trigger component, trading a little flexibility for improved ergonomics:
```
import{MenuTrigger,MenuContent}from'my-design-system';
functionMyMenu({children}){
return(
<MenuTrigger>
<button>OpenMenu</button>
</MenuTrigger>
<MenuContent>{children}</MenuContent>
);
}

```

## The command and commandfor pattern
With the `command` and `commandfor` attributes, buttons can now perform actions on other elements declaratively, bringing the ergonomics of a framework without sacrificing flexibility. The `commandfor` button takes an ID—similar to the `for` attribute—while `command` accepts built-in values, enabling a more portable and intuitive approach.
### Example: An open menu button with command and commandfor
The following HTML sets up declarative relationships between the button and the menu which lets the browser handle the logic and accessibility for you. There's no need to manage `aria-expanded` or add any additional JavaScript.
```
<button commandfor="my-menu" command="show-popover">
Open Menu
</button>
<div popover id="my-menu">
 <!-- ... -->
</div>

```

### Comparing `command` and `commandfor` with `popovertargetaction` and `popovertarget`
If you've used `popover` before, you might be familiar with the `popovertarget` and `popovertargetaction` attributes. These work similarly to `commandfor` and `command` respectively—except they're specific to popovers. The `command` and `commandfor` attributes completely replace these older attributes. The new attributes support everything the older attributes did, as well as adding new capabilities.
## Built-in commands
The `command` attribute has a set of built-in behaviours which map to various APIs for interactive elements:
  * `show-popover`: Maps to `el.showPopover()`.
  * `hide-popover`: Maps to `el.hidePopover()`.
  * `toggle-popover`: Maps to `el.togglePopover()`.
  * `show-modal`: Maps to `dialogEl.showModal()`.
  * `close`: Maps to `dialogEl.close()`.


These commands map to their JavaScript counterparts, while also streamlining accessibility (such as providing the `aria-details` and `aria-expanded` equivalent relations), focus management, and more.
### Example: A confirmation dialog with `command` and `commandfor`
```
<button commandfor="confirm-dialog" command="show-modal">
 Delete Record
</button>
<dialog id="confirm-dialog">
 <header>
  <h1>Delete Record?</h1>
  <button commandfor="confirm-dialog" command="close" aria-label="Close" value="close">
   <img role="none" src="/close-icon.svg">
  </button>
 </header>
 <p>Are you sure? This action cannot be undone</p>
 <footer>
  <button commandfor="confirm-dialog" command="close" value="cancel">
   Cancel
  </button>
  <button commandfor="confirm-dialog" command="close" value="delete">
   Delete
  </button>
 </footer>
</dialog>

```

Clicking the **Delete Record** button will open the dialog as a modal, while clicking the **Close** , **Cancel** , or **Delete** buttons will close the dialog while also dispatching a `"close"` event on the dialog, which has a `returnValue` property matching the button's value. This reduces the need for JavaScript beyond a single event listener on the dialog to determine what to do next:
```
dialog.addEventListener("close",(event)=>{
if(event.target.returnValue=="cancel"){
console.log("cancel was clicked");
}elseif(event.target.returnValue=="close"){
console.log("close was clicked");
}elseif(event.target.returnValue=="delete"){
console.log("delete was clicked");
}
});

```

## Custom commands
In addition to the built-in commands, you can define custom commands using a `--` prefix. Custom commands will dispatch a `"command"` event on the target element (just like the built-in commands), but otherwise will never perform any additional logic like the built-in values do. This gives flexibility for building components that can react to buttons in various ways without having to provide wrapper components, traverse the DOM for the target element, or mapping button clicks to state changes. This lets you provide an API _within_ HTML for your components:
```
<button commandfor="the-image" command="--rotate-landscape">
 Landscape
</button>
<button commandfor="the-image" command="--rotate-portrait">
 Portrait
</button>
<img id="the-image" src="photo.jpg">
<script type="module">
 const image = document.getElementById("the-image");
 image.addEventListener("command", (event) => {
  if ( event.command == "--rotate-landscape" ) {
  image.style.rotate = "-90deg"
  } else if ( event.command == "--rotate-portrait" ) {
  image.style.rotate = "0deg"
  }
 });
</script>

```

## Commands in the ShadowDOM
Given the `commandfor` attribute takes an ID, there are restrictions around crossing the shadow DOM. In these cases you can use the JavaScript API to set the `.commandForElement` property which can set any element, across shadow roots:
```
<my-element>
 <template shadowrootmode=open>
  <button command="show-popover">Show popover</button>
  <slot></slot>
 </template>
 <div popover><!-- ... --></div>
</my-element>
<script>
customElements.define("my-element", class extends HTMLElement {
 connectedCallback() {
  const popover = this.querySelector('[popover]');
  // The commandForElement can set cross-shadow root elements.
  this.shadowRoot.querySelector('button').commandForElement = popover;
 }
});
</script>

```

Future proposals may provide a declarative way to share references across shadow boundaries, such as the [Reference Target Proposal](https://github.com/WICG/webcomponents/blob/gh-pages/proposals/reference-target-explainer.md).
## What's next?
We'll be continuing to explore possibilities for new built-in commands, to cover common functionality that websites use. Proposed ideas are covered in the [Open UI Proposal](https://open-ui.org/components/future-invokers.explainer/). Some of the ideas already explored:
  * Opening and closing `<details>` elements.
  * A `"show-picker"` command for `<input>` and `<select>` elements, mapping to `showPicker()`.
  * Playback commands for `<video>` and `<audio>` elements.
  * Copying text content from elements.


We welcome community input—if you have suggestions don't hesitate to file an issue on the [Open UI Issue Tracker](https://github.com/openui/open-ui/issues/new).
## Learn more
Find more information about `command` and `commandfor` in [the specification](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command) and on [MDN](https://developer.mozilla.org/docs/Web/API/Invoker_Commands_API).
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-03-07 UTC.

