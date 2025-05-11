---
url: https://developer.chrome.com/blog/angular-dom-safety-ssr
title: https://developer.chrome.com/blog/angular-dom-safety-ssr
date: 2025-05-11T16:53:55.218050
depth: 2
---

[ Skip to main content ](https://developer.chrome.com/blog/angular-dom-safety-ssr#main-content)
  * [Español – América Latina](https://developer.chrome.com/blog/angular-dom-safety-ssr?hl=es-419)

Sign in


  * On this page
  * [Avoid manual DOM manipulation](https://developer.chrome.com/blog/angular-dom-safety-ssr#avoid_manual_dom_manipulation)
    * [Mutate a component's own DOM element](https://developer.chrome.com/blog/angular-dom-safety-ssr#mutate_a_components_own_dom_element)
    * [Mutate DOM elements outside of a template](https://developer.chrome.com/blog/angular-dom-safety-ssr#mutate_dom_elements_outside_of_a_template)
  * [Defer manual DOM manipulation](https://developer.chrome.com/blog/angular-dom-safety-ssr#defer_manual_dom_manipulation)
    * [Run browser-only JavaScript](https://developer.chrome.com/blog/angular-dom-safety-ssr#run_browser-only_javascript)
    * [Perform custom layout](https://developer.chrome.com/blog/angular-dom-safety-ssr#perform_custom_layout)


  * [ Chrome for Developers ](https://developer.chrome.com/)


#  Safely accessing the DOM with Angular SSR 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Avoid manual DOM manipulation](https://developer.chrome.com/blog/angular-dom-safety-ssr#avoid_manual_dom_manipulation)
    * [Mutate a component's own DOM element](https://developer.chrome.com/blog/angular-dom-safety-ssr#mutate_a_components_own_dom_element)
    * [Mutate DOM elements outside of a template](https://developer.chrome.com/blog/angular-dom-safety-ssr#mutate_dom_elements_outside_of_a_template)
  * [Defer manual DOM manipulation](https://developer.chrome.com/blog/angular-dom-safety-ssr#defer_manual_dom_manipulation)
    * [Run browser-only JavaScript](https://developer.chrome.com/blog/angular-dom-safety-ssr#run_browser-only_javascript)
    * [Perform custom layout](https://developer.chrome.com/blog/angular-dom-safety-ssr#perform_custom_layout)


Gerald Monaco 
[ GitHub ](https://github.com/devknoll)
Over the last year, Angular has gained many new features such as [hydration](https://angular.dev/guide/hydration) and [deferrable views](https://angular.dev/guide/defer) to help developers improve their [Core Web Vitals](https://web.dev/explore/learn-core-web-vitals) and ensure a great experience for their end users. Research into additional server-side rendering related features that build on this functionality is also underway, such as streaming and partial hydration.
Unfortunately, there is one pattern that might prevent your application or library from taking full advantage of all these new and upcoming features: manual manipulation of the underlying DOM structure. Angular requires that the structure of the DOM remains consistent from the time a component is serialized by the server, until it is hydrated on the browser. Using [`ElementRef`](https://angular.dev/api/core/ElementRef), [`Renderer2`](https://angular.dev/api/core/Renderer2), or DOM APIs to manually add, move, or remove nodes from the DOM before hydration can introduce inconsistencies that prevent these features from working.
However, not all manual DOM manipulation and access is problematic, and sometimes it's necessary. The key to using the DOM safely is to minimize your need for it as much as possible, and then defer your usage of it as long as possible. The following guidelines explain how you can accomplish this and build truly universal and future-proof Angular components that can take full advantage of all of Angular's new and upcoming features.
## Avoid manual DOM manipulation
The best way to avoid the issues that manual DOM manipulation causes is, unsurprisingly, to avoid it altogether wherever possible. Angular has built-in APIs and patterns that can manipulate most aspects of the DOM: you should prefer using them instead of accessing the DOM directly.
### Mutate a component's own DOM element
When writing a component or directive, you may need to modify the _host element_ (that is, the DOM element that matches the component or directive's _selector_) to, for example, add a class, style, or attribute, rather than targeting or introducing a wrapper element. It's tempting to just reach for `ElementRef` to mutate the underlying DOM element. Instead, you should use _host bindings_ to _declaratively_ bind the values to an expression:
```
@Component({
selector:'my-component',
template:`...`,
host:{
'[class.foo]':'true'
},
})
exportclassMyComponent{
/* ... */
}

```

Just as with [data binding in HTML](https://angular.io/guide/binding-syntax), you can also, for example, bind to attributes and styles, and change `'true'` to a different expression that Angular will use to automatically add or remove the value as needed.
In some cases, the _key_ will need to be computed dynamically. You can _also_ bind to a signal or function that returns a set or map of values:
```
@Component({
selector:'my-component',
template:`...`,
host:{
'[class.foo]':'true',
'[class]':'classes()'
},
})
exportclassMyComponent{
size=signal('large');
classes=computed(()=>{
return[`size-${this.size()}`];
});
}

```

In more complex applications, it may be tempting to reach for manual DOM manipulation to avoid an [`ExpressionChangedAfterItHasBeenCheckedError`](https://angular.dev/errors/NG0100). Instead, you can bind the value to a signal as in the previous example. This can be done as needed, and doesn't require adopting signals across your entire codebase.
### Mutate DOM elements outside of a template
It's tempting to try to use the DOM to access elements that aren't normally accessible, such as those that belong to other parent or child components. However, this is error prone, violates encapsulation, and makes it difficult to change or upgrade those components in the future.
Instead, your component should consider every other component to be a [black box](https://en.wikipedia.org/wiki/Black_box). Take the time to consider when and where other components (even within the same application or library) may need to interact with or customize your component's behavior or appearance, and then expose a safe and documented way to do so. Use features like [hierarchical dependency injection](https://angular.dev/guide/di/hierarchical-dependency-injection) to make an API available to a subtree when simple [`@Input`](https://angular.dev/api/core/Input) and [`@Output`](https://angular.dev/api/core/Output) properties aren't sufficient.
Historically, it was common to implement features like modal dialogs or tooltips by adding an element to the end of the `<body>` or some other host element and then moving or projecting content there. However, these days you can likely render a simple [`<dialog>`](https://developer.mozilla.org/docs/Web/HTML/Element/dialog) element in your template instead:
```
@Component({
selector:'my-component',
template:`<dialog #dialog>Hello World</dialog>`,
})
exportclassMyComponent{
@ViewChild('dialog')dialogRef!:ElementRef;
constructor(){
afterNextRender(()=>{
this.dialogRef.nativeElement.showModal();
});
}
}

```

## Defer manual DOM manipulation
After using the previous guidelines to minimize your direct DOM manipulation and access as much as possible, you may have some remaining that is unavoidable. In such cases, it's important to defer it as long as possible. [`afterRender`](https://angular.dev/api/core/afterRender) and [`afterNextRender`](https://angular.dev/api/core/afterNextRender) callbacks are a great way to do this, as they only run on the browser, after Angular has checked for any changes and committed them to the DOM.
### Run browser-only JavaScript
In some cases you will have a library or API that only works in the browser (for example, a chart library, some `IntersectionObserver` usage, etc). Instead of conditionally checking whether you're running on the browser, or stubbing out behavior on the server, you can just use `afterNextRender`:
```
@Component({
/* ... */
})
exportclassMyComponent{
@ViewChild('chart')chartRef:ElementRef;
myChart:MyChart|null=null;
constructor(){
afterNextRender(()=>{
this.myChart=newMyChart(this.chartRef.nativeElement);
});
}
}

```

### Perform custom layout
Sometimes you may need to read or write to the DOM to perform some layout that your target browsers don't support yet, such as positioning a tooltip. `afterRender` is a great choice for this, as you can be certain that the DOM is in a consistent state. `afterRender` and `afterNextRender` accept a [`phase`](https://angular.dev/api/core/AfterRenderPhase) value of `EarlyRead`, `Read`, or `Write`. Reading the DOM layout after writing it forces the browser to synchronously recalculate the layout, which can seriously affect performance (see: [layout thrashing](https://web.dev/articles/avoid-large-complex-layouts-and-layout-thrashing)). Therefore it's important to carefully split your logic into the correct phases.
For example, a tooltip component that wants to display a tooltip relative to another element on the page would likely use two phases. The `EarlyRead` phase would first be used to acquire the size and position of the elements:
```
afterRender(()=>{
targetRect=targetEl.getBoundingClientRect();
tooltipRect=tooltipEl.getBoundingClientRect();
},{phase:AfterRenderPhase.EarlyRead},
);

```

Then, the `Write` phase would use the previously read value to actually reposition the tooltip:
```
afterRender(()=>{
tooltipEl.style.setProperty('left',`${targetRect.left+targetRect.width/2-tooltipRect.width/2}px`);
tooltipEl.style.setProperty('top',`${targetRect.bottom-4}px`);
},{phase:AfterRenderPhase.Write},
);

```

By splitting our logic into the correct phases, Angular is able to effectively batch DOM manipulation across every other component in the application, ensuring a minimal performance impact.
## Conclusion
There are many new and exciting improvements to Angular server-side rendering on the horizon, with the goal of making it easier for you to provide a great experience for your users. We hope that the previous tips will prove useful in helping you take full advantage of them in your applications and libraries!
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2024-01-17 UTC.

