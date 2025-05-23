---
url: https://reactnative.dev/docs/intro-react
title: https://reactnative.dev/docs/intro-react
date: 2025-05-10T21:40:25.789304
depth: 2
---

[Skip to main content](https://reactnative.dev/docs/intro-react#__docusaurus_skipToContent_fallback)
Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).
On this page
React Native runs on [React](https://react.dev/), a popular open source library for building user interfaces with JavaScript. To make the most of React Native, it helps to understand React itself. This section can get you started or can serve as a refresher course.
We’re going to cover the core concepts behind React:
  * components
  * JSX
  * props
  * state


If you want to dig deeper, we encourage you to check out [React’s official documentation](https://react.dev/learn).
## Your first component[​](https://reactnative.dev/docs/intro-react#your-first-component "Direct link to Your first component")
The rest of this introduction to React uses cats in its examples: friendly, approachable creatures that need names and a cafe to work in. Here is your very first Cat component:
Here is how you do it: To define your `Cat` component, first use JavaScript’s [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import) to import React and React Native’s [`Text`](https://reactnative.dev/docs/next/text) Core Component:
tsx
```
importReactfrom'react';import{Text}from'react-native';
```

Your component starts as a function:
tsx
```
constCat=()=>{};
```

You can think of components as blueprints. Whatever a function component returns is rendered as a **React element.** React elements let you describe what you want to see on the screen.
Here the `Cat` component will render a `<Text>` element:
tsx
```
constCat=()=>{return<Text>Hello, I am your cat!</Text>;
```

You can export your function component with JavaScript’s [`export default`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export) for use throughout your app like so:
tsx
```
constCat=()=>{return<Text>Hello, I am your cat!</Text>;exportdefaultCat;
```

> This is one of many ways to export your component. This kind of export works well with the Snack Player. However, depending on your app’s file structure, you might need to use a different convention. This [handy cheatsheet on JavaScript imports and exports](https://medium.com/dailyjs/javascript-module-cheatsheet-7bd474f1d829) can help.
Now take a closer look at that `return` statement. `<Text>Hello, I am your cat!</Text>` is using a kind of JavaScript syntax that makes writing elements convenient: JSX.
## JSX[​](https://reactnative.dev/docs/intro-react#jsx "Direct link to JSX")
React and React Native use **JSX,** a syntax that lets you write elements inside JavaScript like so: `<Text>Hello, I am your cat!</Text>`. The React docs have [a comprehensive guide to JSX](https://react.dev/learn/writing-markup-with-jsx) you can refer to learn even more. Because JSX is JavaScript, you can use variables inside it. Here you are declaring a name for the cat, `name`, and embedding it with curly braces inside `<Text>`.
Any JavaScript expression will work between curly braces, including function calls like `{getFullName("Rum", "Tum", "Tugger")}`:
  * TypeScript
  * JavaScript


You can think of curly braces as creating a portal into JS functionality in your JSX!
> Because JSX is included in the React library, it won’t work if you don’t have `import React from 'react'` at the top of your file!
## Custom Components[​](https://reactnative.dev/docs/intro-react#custom-components "Direct link to Custom Components")
You’ve already met [React Native’s Core Components](https://reactnative.dev/docs/intro-react-native-components). React lets you nest these components inside each other to create new components. These nestable, reusable components are at the heart of the React paradigm.
For example, you can nest [`Text`](https://reactnative.dev/docs/text) and [`TextInput`](https://reactnative.dev/docs/textinput) inside a [`View`](https://reactnative.dev/docs/view) below, and React Native will render them together:
#### Developer notes[​](https://reactnative.dev/docs/intro-react#developer-notes "Direct link to Developer notes")
  * Android
  * Web


> If you’re familiar with web development, `<View>` and `<Text>` might remind you of HTML! You can think of them as the `<div>` and `<p>` tags of application development.
> On Android, you usually put your views inside `LinearLayout`, `FrameLayout`, `RelativeLayout`, etc. to define how the view’s children will be arranged on the screen. In React Native, `View` uses Flexbox for its children’s layout. You can learn more in [our guide to layout with Flexbox](https://reactnative.dev/docs/flexbox).
You can render this component multiple times and in multiple places without repeating your code by using `<Cat>`:
Any component that renders other components is a **parent component.** Here, `Cafe` is the parent component and each `Cat` is a **child component.**
You can put as many cats in your cafe as you like. Each `<Cat>` renders a unique element—which you can customize with props.
## Props[​](https://reactnative.dev/docs/intro-react#props "Direct link to Props")
**Props** is short for “properties”. Props let you customize React components. For example, here you pass each `<Cat>` a different `name` for `Cat` to render:
  * TypeScript
  * JavaScript


Most of React Native’s Core Components can be customized with props, too. For example, when using [`Image`](https://reactnative.dev/docs/image), you pass it a prop named [`source`](https://reactnative.dev/docs/image#source) to define what image it shows:
`Image` has [many different props](https://reactnative.dev/docs/image#props), including [`style`](https://reactnative.dev/docs/image#style), which accepts a JS object of design and layout related property-value pairs.
> Notice the double curly braces `{{ }}` surrounding `style`‘s width and height. In JSX, JavaScript values are referenced with `{}`. This is handy if you are passing something other than a string as props, like an array or number: `<Cat food={["fish", "kibble"]} age={2} />`. However, JS objects are **_also_** denoted with curly braces: `{width: 200, height: 200}`. Therefore, to pass a JS object in JSX, you must wrap the object in **another pair** of curly braces: `{{width: 200, height: 200}}`
You can build many things with props and the Core Components [`Text`](https://reactnative.dev/docs/text), [`Image`](https://reactnative.dev/docs/image), and [`View`](https://reactnative.dev/docs/view)! But to build something interactive, you’ll need state.
## State[​](https://reactnative.dev/docs/intro-react#state "Direct link to State")
While you can think of props as arguments you use to configure how components render, **state** is like a component’s personal data storage. State is useful for handling data that changes over time or that comes from user interaction. State gives your components memory!
> As a general rule, use props to configure a component when it renders. Use state to keep track of any component data that you expect to change over time.
The following example takes place in a cat cafe where two hungry cats are waiting to be fed. Their hunger, which we expect to change over time (unlike their names), is stored as state. To feed the cats, press their buttons—which will update their state.
You can add state to a component by calling [React’s `useState` Hook](https://react.dev/learn/state-a-components-memory). A Hook is a kind of function that lets you “hook into” React features. For example, `useState` is a Hook that lets you add state to function components. You can learn more about [other kinds of Hooks in the React documentation.](https://react.dev/reference/react)
  * TypeScript
  * JavaScript


First, you will want to import `useState` from React like so:
tsx
```
importReact,{useState}from'react';
```

Then you declare the component’s state by calling `useState` inside its function. In this example, `useState` creates an `isHungry` state variable:
tsx
```
constCat=(props:CatProps)=>{const[isHungry, setIsHungry]=useState(true);// ...
```

> You can use `useState` to track any kind of data: strings, numbers, Booleans, arrays, objects. For example, you can track the number of times a cat has been petted with `const [timesPetted, setTimesPetted] = useState(0)`!
Calling `useState` does two things:
  * it creates a “state variable” with an initial value—in this case the state variable is `isHungry` and its initial value is `true`
  * it creates a function to set that state variable’s value—`setIsHungry`


It doesn’t matter what names you use. But it can be handy to think of the pattern as `[<getter>, <setter>] = useState(<initialValue>)`.
Next you add the [`Button`](https://reactnative.dev/docs/button) Core Component and give it an `onPress` prop:
tsx
```
<ButtononPress={()=>{setIsHungry(false);//../>
```

Now, when someone presses the button, `onPress` will fire, calling the `setIsHungry(false)`. This sets the state variable `isHungry` to `false`. When `isHungry` is false, the `Button`’s `disabled` prop is set to `true` and its `title` also changes:
tsx
```
<Button//..disabled={!isHungry}title={isHungry ?'Give me some food, please!':'Thank you!'}/>
```

> You might’ve noticed that although `isHungry` is a [const](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/const), it is seemingly reassignable! What is happening is when a state-setting function like `setIsHungry` is called, its component will re-render. In this case the `Cat` function will run again—and this time, `useState` will give us the next value of `isHungry`.
Finally, put your cats inside a `Cafe` component:
tsx
```
constCafe=()=>{return(<Catname="Munkustrap"/><Catname="Spot"/></>
```

> See the `<>` and `</>` above? These bits of JSX are [fragments](https://react.dev/reference/react/Fragment). Adjacent JSX elements must be wrapped in an enclosing tag. Fragments let you do that without nesting an extra, unnecessary wrapping element like `View`.
Now that you’ve covered both React and React Native’s Core Components, let’s dive deeper on some of these core components by looking at [handling `<TextInput>`](https://reactnative.dev/docs/handling-text-input).
Is this page useful?
  * [Your first component](https://reactnative.dev/docs/intro-react#your-first-component)
  * [Custom Components](https://reactnative.dev/docs/intro-react#custom-components)



