---
url: https://reactnative.dev/docs/virtualizedlist
title: https://reactnative.dev/docs/virtualizedlist
date: 2025-05-10T21:42:58.412693
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/virtualizedlist#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
Base implementation for the more convenient [`<FlatList>`](https://reactnative.dev/docs/flatlist) and [`<SectionList>`](https://reactnative.dev/docs/sectionlist) components, which are also better documented. In general, this should only really be used if you need more flexibility than [`FlatList`](https://reactnative.dev/docs/flatlist) provides, e.g. for use with immutable data instead of plain arrays.
Virtualization massively improves memory consumption and performance of large lists by maintaining a finite render window of active items and replacing all items outside of the render window with appropriately sized blank space. The window adapts to scrolling behavior, and items are rendered incrementally with low-pri (after any running interactions) if they are far from the visible area, or with hi-pri otherwise to minimize the potential of seeing blank space.
## Example[​](https://reactnative.dev/docs/virtualizedlist#example "Direct link to Example")
  * TypeScript
  * JavaScript


Some caveats:
  * Internal state is not preserved when content scrolls out of the render window. Make sure all your data is captured in the item data or external stores like Flux, Redux, or Relay.
  * This is a `PureComponent` which means that it will not re-render if `props` are shallow-equal. Make sure that everything your `renderItem` function depends on is passed as a prop (e.g. `extraData`) that is not `===` after updates, otherwise your UI may not update on changes. This includes the `data` prop and parent component state.
  * In order to constrain memory and enable smooth scrolling, content is rendered asynchronously offscreen. This means it's possible to scroll faster than the fill rate and momentarily see blank content. This is a tradeoff that can be adjusted to suit the needs of each application, and we are working on improving it behind the scenes.
  * By default, the list looks for a `key` prop on each item and uses that for the React key. Alternatively, you can provide a custom `keyExtractor` prop.


# Reference
## Props[​](https://reactnative.dev/docs/virtualizedlist#props "Direct link to Props")
### [ScrollView Props](https://reactnative.dev/docs/scrollview#props)[​](https://reactnative.dev/docs/virtualizedlist#scrollview-props "Direct link to scrollview-props")
Inherits [ScrollView Props](https://reactnative.dev/docs/scrollview#props).
### `data`[​](https://reactnative.dev/docs/virtualizedlist#data "Direct link to data")
Opaque data type passed to `getItem` and `getItemCount` to retrieve items.
Type  
---  
any  
### 
Required
**`getItem`**[​](https://reactnative.dev/docs/virtualizedlist#required-getitem "Direct link to required-getitem")
tsx
```
(data:any, index:number)=>any;
```

A generic accessor for extracting an item from any sort of data blob.
Type  
---  
function  
### 
Required
**`getItemCount`**[​](https://reactnative.dev/docs/virtualizedlist#required-getitemcount "Direct link to required-getitemcount")
tsx
```
(data:any)=>number;
```

Determines how many items are in the data blob.
Type  
---  
function  
### 
Required
**`renderItem`**[​](https://reactnative.dev/docs/virtualizedlist#required-renderitem "Direct link to required-renderitem")
tsx
```
(info:any)=>?React.Element<any>
```

Takes an item from `data` and renders it into the list
Type  
---  
function  
### `CellRendererComponent`[​](https://reactnative.dev/docs/virtualizedlist#cellrenderercomponent "Direct link to cellrenderercomponent")
CellRendererComponent allows customizing how cells rendered by `renderItem`/`ListItemComponent` are wrapped when placed into the underlying ScrollView. This component must accept event handlers which notify VirtualizedList of changes within the cell.
Type  
---  
`React.ComponentType<CellRendererProps>`  
### `ItemSeparatorComponent`[​](https://reactnative.dev/docs/virtualizedlist#itemseparatorcomponent "Direct link to itemseparatorcomponent")
Rendered in between each item, but not at the top or bottom. By default, `highlighted` and `leadingItem` props are provided. `renderItem` provides `separators.highlight`/`unhighlight` which will update the `highlighted` prop, but you can also add custom props with `separators.updateProps`. Can be a React Component (e.g. `SomeComponent`), or a React element (e.g. `<SomeComponent />`).
Type  
---  
component, function, element  
### `ListEmptyComponent`[​](https://reactnative.dev/docs/virtualizedlist#listemptycomponent "Direct link to listemptycomponent")
Rendered when the list is empty. Can be a React Component (e.g. `SomeComponent`), or a React element (e.g. `<SomeComponent />`).
Type  
---  
component, element  
### `ListItemComponent`[​](https://reactnative.dev/docs/virtualizedlist#listitemcomponent "Direct link to listitemcomponent")
Each data item is rendered using this element. Can be a React Component Class, or a render function.
Type  
---  
component, function  
### `ListFooterComponent`[​](https://reactnative.dev/docs/virtualizedlist#listfootercomponent "Direct link to listfootercomponent")
Rendered at the bottom of all the items. Can be a React Component (e.g. `SomeComponent`), or a React element (e.g. `<SomeComponent />`).
Type  
---  
component, element  
### `ListFooterComponentStyle`[​](https://reactnative.dev/docs/virtualizedlist#listfootercomponentstyle "Direct link to listfootercomponentstyle")
Styling for internal View for `ListFooterComponent`.
Type| Required  
---|---  
ViewStyleProp| No  
### `ListHeaderComponent`[​](https://reactnative.dev/docs/virtualizedlist#listheadercomponent "Direct link to listheadercomponent")
Rendered at the top of all the items. Can be a React Component (e.g. `SomeComponent`), or a React element (e.g. `<SomeComponent />`).
Type  
---  
component, element  
### `ListHeaderComponentStyle`[​](https://reactnative.dev/docs/virtualizedlist#listheadercomponentstyle "Direct link to listheadercomponentstyle")
Styling for internal View for `ListHeaderComponent`.
Type  
---  
### `debug`[​](https://reactnative.dev/docs/virtualizedlist#debug "Direct link to debug")
`debug` will turn on extra logging and visual overlays to aid with debugging both usage and implementation, but with a significant perf hit.
Type  
---  
boolean  
### `disableVirtualization`[​](https://reactnative.dev/docs/virtualizedlist#disablevirtualization "Direct link to disablevirtualization")
> **Deprecated.** Virtualization provides significant performance and memory optimizations, but fully unmounts react instances that are outside of the render window. You should only need to disable this for debugging purposes.
Type  
---  
boolean  
### `extraData`[​](https://reactnative.dev/docs/virtualizedlist#extradata "Direct link to extradata")
A marker property for telling the list to re-render (since it implements `PureComponent`). If any of your `renderItem`, Header, Footer, etc. functions depend on anything outside of the `data` prop, stick it here and treat it immutably.
Type  
---  
any  
### `getItemLayout`[​](https://reactnative.dev/docs/virtualizedlist#getitemlayout "Direct link to getitemlayout")
tsx
```
 data:any, index:number,)=>{length:number, offset:number, index:number}
```

Type  
---  
function  
### `horizontal`[​](https://reactnative.dev/docs/virtualizedlist#horizontal "Direct link to horizontal")
If `true`, renders items next to each other horizontally instead of stacked vertically.
Type  
---  
boolean  
### `initialNumToRender`[​](https://reactnative.dev/docs/virtualizedlist#initialnumtorender "Direct link to initialnumtorender")
How many items to render in the initial batch. This should be enough to fill the screen but not much more. Note these items will never be unmounted as part of the windowed rendering in order to improve perceived performance of scroll-to-top actions.
Type| Default  
---|---  
number| `10`  
### `initialScrollIndex`[​](https://reactnative.dev/docs/virtualizedlist#initialscrollindex "Direct link to initialscrollindex")
Instead of starting at the top with the first item, start at `initialScrollIndex`. This disables the "scroll to top" optimization that keeps the first `initialNumToRender` items always rendered and immediately renders the items starting at this initial index. Requires `getItemLayout` to be implemented.
Type  
---  
number  
### `inverted`[​](https://reactnative.dev/docs/virtualizedlist#inverted "Direct link to inverted")
Reverses the direction of scroll. Uses scale transforms of `-1`.
Type  
---  
boolean  
### `keyExtractor`[​](https://reactnative.dev/docs/virtualizedlist#keyextractor "Direct link to keyextractor")
tsx
```
(item:any, index:number)=>string;
```

Used to extract a unique key for a given item at the specified index. Key is used for caching and as the react key to track item re-ordering. The default extractor checks `item.key`, then `item.id`, and then falls back to using the index, like React does.
Type  
---  
function  
### `maxToRenderPerBatch`[​](https://reactnative.dev/docs/virtualizedlist#maxtorenderperbatch "Direct link to maxtorenderperbatch")
The maximum number of items to render in each incremental render batch. The more rendered at once, the better the fill rate, but responsiveness may suffer because rendering content may interfere with responding to button taps or other interactions.
Type  
---  
number  
### `onEndReached`[​](https://reactnative.dev/docs/virtualizedlist#onendreached "Direct link to onendreached")
Called once when the scroll position gets within `onEndReachedThreshold` from the logical end of the list.
Type  
---  
`(info: {distanceFromEnd: number}) => void`  
### `onEndReachedThreshold`[​](https://reactnative.dev/docs/virtualizedlist#onendreachedthreshold "Direct link to onendreachedthreshold")
How far from the end (in units of visible length of the list) the trailing edge of the list must be from the end of the content to trigger the `onEndReached` callback. Thus, a value of 0.5 will trigger `onEndReached` when the end of the content is within half the visible length of the list.
Type| Default  
---|---  
number  
### `onRefresh`[​](https://reactnative.dev/docs/virtualizedlist#onrefresh "Direct link to onrefresh")
tsx
```
()=>void;
```

If provided, a standard `RefreshControl` will be added for "Pull to Refresh" functionality. Make sure to also set the `refreshing` prop correctly.
Type  
---  
function  
### `onScrollToIndexFailed`[​](https://reactnative.dev/docs/virtualizedlist#onscrolltoindexfailed "Direct link to onscrolltoindexfailed")
tsx
```
(info:{ index:number, highestMeasuredFrameIndex:number, averageItemLength:number,})=>void;
```

Used to handle failures when scrolling to an index that has not been measured yet. Recommended action is to either compute your own offset and `scrollTo` it, or scroll as far as possible and then try again after more items have been rendered.
Type  
---  
function  
### `onStartReached`[​](https://reactnative.dev/docs/virtualizedlist#onstartreached "Direct link to onstartreached")
Called once when the scroll position gets within `onStartReachedThreshold` from the logical start of the list.
Type  
---  
`(info: {distanceFromStart: number}) => void`  
### `onStartReachedThreshold`[​](https://reactnative.dev/docs/virtualizedlist#onstartreachedthreshold "Direct link to onstartreachedthreshold")
How far from the start (in units of visible length of the list) the leading edge of the list must be from the start of the content to trigger the `onStartReached` callback. Thus, a value of 0.5 will trigger `onStartReached` when the start of the content is within half the visible length of the list.
Type| Default  
---|---  
number  
### `onViewableItemsChanged`[​](https://reactnative.dev/docs/virtualizedlist#onviewableitemschanged "Direct link to onviewableitemschanged")
Called when the viewability of rows changes, as defined by the `viewabilityConfig` prop.
Type  
---  
`(callback: {changed: ViewToken[](https://reactnative.dev/docs/viewtoken)[], viewableItems: ViewToken[](https://reactnative.dev/docs/viewtoken)[]}) => void`  
### `persistentScrollbar`[​](https://reactnative.dev/docs/virtualizedlist#persistentscrollbar "Direct link to persistentscrollbar")
Type  
---  
bool  
### `progressViewOffset`[​](https://reactnative.dev/docs/virtualizedlist#progressviewoffset "Direct link to progressviewoffset")
Set this when offset is needed for the loading indicator to show correctly.
Type  
---  
number  
### `refreshControl`[​](https://reactnative.dev/docs/virtualizedlist#refreshcontrol "Direct link to refreshcontrol")
A custom refresh control element. When set, it overrides the default `<RefreshControl>` component built internally. The onRefresh and refreshing props are also ignored. Only works for vertical VirtualizedList.
Type  
---  
element  
### `refreshing`[​](https://reactnative.dev/docs/virtualizedlist#refreshing "Direct link to refreshing")
Set this true while waiting for new data from a refresh.
Type  
---  
boolean  
### `removeClippedSubviews`[​](https://reactnative.dev/docs/virtualizedlist#removeclippedsubviews "Direct link to removeclippedsubviews")
This may improve scroll performance for large lists.
> Note: May have bugs (missing content) in some circumstances - use at your own risk.
Type  
---  
boolean  
### `renderScrollComponent`[​](https://reactnative.dev/docs/virtualizedlist#renderscrollcomponent "Direct link to renderscrollcomponent")
tsx
```
(props: object)=> element;
```

Render a custom scroll component, e.g. with a differently styled `RefreshControl`.
Type  
---  
function  
### `viewabilityConfig`[​](https://reactnative.dev/docs/virtualizedlist#viewabilityconfig "Direct link to viewabilityconfig")
See `ViewabilityHelper.js` for flow type and further documentation.
Type  
---  
ViewabilityConfig  
### `viewabilityConfigCallbackPairs`[​](https://reactnative.dev/docs/virtualizedlist#viewabilityconfigcallbackpairs "Direct link to viewabilityconfigcallbackpairs")
List of `ViewabilityConfig`/`onViewableItemsChanged` pairs. A specific `onViewableItemsChanged` will be called when its corresponding `ViewabilityConfig`'s conditions are met. See `ViewabilityHelper.js` for flow type and further documentation.
Type  
---  
array of ViewabilityConfigCallbackPair  
### `updateCellsBatchingPeriod`[​](https://reactnative.dev/docs/virtualizedlist#updatecellsbatchingperiod "Direct link to updatecellsbatchingperiod")
Amount of time between low-pri item render batches, e.g. for rendering items quite a ways off screen. Similar fill rate/responsiveness tradeoff as `maxToRenderPerBatch`.
Type  
---  
number  
### `windowSize`[​](https://reactnative.dev/docs/virtualizedlist#windowsize "Direct link to windowsize")
Determines the maximum number of items rendered outside of the visible area, in units of visible lengths. So if your list fills the screen, then `windowSize={21}` (the default) will render the visible screen area plus up to 10 screens above and 10 below the viewport. Reducing this number will reduce memory consumption and may improve performance, but will increase the chance that fast scrolling may reveal momentary blank areas of unrendered content.
Type  
---  
number  
## Methods[​](https://reactnative.dev/docs/virtualizedlist#methods "Direct link to Methods")
### `flashScrollIndicators()`[​](https://reactnative.dev/docs/virtualizedlist#flashscrollindicators "Direct link to flashscrollindicators")
tsx
```
flashScrollIndicators();
```

### `getScrollableNode()`[​](https://reactnative.dev/docs/virtualizedlist#getscrollablenode "Direct link to getscrollablenode")
tsx
```
getScrollableNode():any;
```

### `getScrollRef()`[​](https://reactnative.dev/docs/virtualizedlist#getscrollref "Direct link to getscrollref")
tsx
```
getScrollRef():|React.ElementRef<typeofScrollView>|React.ElementRef<typeofView>|null;
```

### `getScrollResponder()`[​](https://reactnative.dev/docs/virtualizedlist#getscrollresponder "Direct link to getscrollresponder")
tsx
```
getScrollResponder()=>ScrollResponderMixin|null;
```

Provides a handle to the underlying scroll responder. Note that `this._scrollRef` might not be a `ScrollView`, so we need to check that it responds to `getScrollResponder` before calling it.
### `scrollToEnd()`[​](https://reactnative.dev/docs/virtualizedlist#scrolltoend "Direct link to scrolltoend")
tsx
```
scrollToEnd(params?:{animated?:boolean});
```

Scrolls to the end of the content. May be janky without `getItemLayout` prop.
**Parameters:**
Name| Type  
---|---  
params| object  
Valid `params` keys are:
  * `'animated'` (boolean) - Whether the list should do an animation while scrolling. Defaults to `true`.


### `scrollToIndex()`[​](https://reactnative.dev/docs/virtualizedlist#scrolltoindex "Direct link to scrolltoindex")
tsx
```
scrollToIndex(params:{ index:number; animated?:boolean; viewOffset?:number; viewPosition?:number;});
```

Valid `params` consist of:
  * 'index' (number). Required.
  * 'animated' (boolean). Optional.
  * 'viewOffset' (number). Optional.
  * 'viewPosition' (number). Optional.


### `scrollToItem()`[​](https://reactnative.dev/docs/virtualizedlist#scrolltoitem "Direct link to scrolltoitem")
tsx
```
scrollToItem(params:{ item:ItemT; animated?:boolean; viewOffset?:number; viewPosition?:number;
```

Valid `params` consist of:
  * 'item' (Item). Required.
  * 'animated' (boolean). Optional.
  * 'viewOffset' (number). Optional.
  * 'viewPosition' (number). Optional.


### `scrollToOffset()`[​](https://reactnative.dev/docs/virtualizedlist#scrolltooffset "Direct link to scrolltooffset")
tsx
```
scrollToOffset(params:{ offset:number; animated?:boolean;});
```

Scroll to a specific content pixel offset in the list.
Param `offset` expects the offset to scroll to. In case of `horizontal` is true, the offset is the x-value, in any other case the offset is the y-value.
Param `animated` (`true` by default) defines whether the list should do an animation while scrolling.
Is this page useful?
  * [Props](https://reactnative.dev/docs/virtualizedlist#props)
    * [ScrollView Props](https://reactnative.dev/docs/virtualizedlist#scrollview-props)
    * [Required **`getItem`**](https://reactnative.dev/docs/virtualizedlist#required-getitem)
    * [Required **`getItemCount`**](https://reactnative.dev/docs/virtualizedlist#required-getitemcount)
    * [Required **`renderItem`**](https://reactnative.dev/docs/virtualizedlist#required-renderitem)
    * [`CellRendererComponent`](https://reactnative.dev/docs/virtualizedlist#cellrenderercomponent)
    * [`ItemSeparatorComponent`](https://reactnative.dev/docs/virtualizedlist#itemseparatorcomponent)
    * [`ListEmptyComponent`](https://reactnative.dev/docs/virtualizedlist#listemptycomponent)
    * [`ListItemComponent`](https://reactnative.dev/docs/virtualizedlist#listitemcomponent)
    * [`ListFooterComponent`](https://reactnative.dev/docs/virtualizedlist#listfootercomponent)
    * [`ListFooterComponentStyle`](https://reactnative.dev/docs/virtualizedlist#listfootercomponentstyle)
    * [`ListHeaderComponent`](https://reactnative.dev/docs/virtualizedlist#listheadercomponent)
    * [`ListHeaderComponentStyle`](https://reactnative.dev/docs/virtualizedlist#listheadercomponentstyle)
    * [`disableVirtualization`](https://reactnative.dev/docs/virtualizedlist#disablevirtualization)
    * [`initialNumToRender`](https://reactnative.dev/docs/virtualizedlist#initialnumtorender)
    * [`initialScrollIndex`](https://reactnative.dev/docs/virtualizedlist#initialscrollindex)
    * [`maxToRenderPerBatch`](https://reactnative.dev/docs/virtualizedlist#maxtorenderperbatch)
    * [`onEndReachedThreshold`](https://reactnative.dev/docs/virtualizedlist#onendreachedthreshold)
    * [`onScrollToIndexFailed`](https://reactnative.dev/docs/virtualizedlist#onscrolltoindexfailed)
    * [`onStartReachedThreshold`](https://reactnative.dev/docs/virtualizedlist#onstartreachedthreshold)
    * [`onViewableItemsChanged`](https://reactnative.dev/docs/virtualizedlist#onviewableitemschanged)
    * [`persistentScrollbar`](https://reactnative.dev/docs/virtualizedlist#persistentscrollbar)
    * [`progressViewOffset`](https://reactnative.dev/docs/virtualizedlist#progressviewoffset)
    * [`removeClippedSubviews`](https://reactnative.dev/docs/virtualizedlist#removeclippedsubviews)
    * [`renderScrollComponent`](https://reactnative.dev/docs/virtualizedlist#renderscrollcomponent)
    * [`viewabilityConfig`](https://reactnative.dev/docs/virtualizedlist#viewabilityconfig)
    * [`viewabilityConfigCallbackPairs`](https://reactnative.dev/docs/virtualizedlist#viewabilityconfigcallbackpairs)
    * [`updateCellsBatchingPeriod`](https://reactnative.dev/docs/virtualizedlist#updatecellsbatchingperiod)
  * [Methods](https://reactnative.dev/docs/virtualizedlist#methods)
    * [`flashScrollIndicators()`](https://reactnative.dev/docs/virtualizedlist#flashscrollindicators)
    * [`getScrollableNode()`](https://reactnative.dev/docs/virtualizedlist#getscrollablenode)
    * [`getScrollResponder()`](https://reactnative.dev/docs/virtualizedlist#getscrollresponder)
    * [`scrollToIndex()`](https://reactnative.dev/docs/virtualizedlist#scrolltoindex)
    * [`scrollToOffset()`](https://reactnative.dev/docs/virtualizedlist#scrolltooffset)



