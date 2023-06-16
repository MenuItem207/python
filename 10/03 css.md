CSS Basics: A Beginner's Guide
==============================

CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation and styling of HTML documents. It allows you to control the layout, appearance, and design of your webpages. In this tutorial, we'll cover some of the fundamental concepts and syntax of CSS.

1. CSS Syntax and Selectors
---------------------------

CSS uses a set of rules to apply styles to HTML elements. Each rule consists of a selector and a declaration block.

- Selectors: Selectors target the HTML elements to which you want to apply styles. There are various types of selectors, including element selectors, class selectors, ID selectors, and more. Here are a few examples:

  - Element selector: `h1` targets all `<h1>` elements.
  - Class selector: `.my-class` targets elements with the class name `my-class`.
  - ID selector: `#my-id` targets the element with the ID `my-id`.

- Declaration Block: The declaration block contains one or more property-value pairs enclosed in curly braces `{}`. Each property defines a specific style aspect, and the value sets the desired value for that property. Here's an example:

  ```css
  h1 {
    color: blue;
    font-size: 24px;
  }
  ```

2. Applying Styles
------------------

You can apply styles to HTML elements using CSS properties. Here are a few commonly used properties:

- `color`: Sets the text color.
- `font-size`: Defines the size of the font.
- `background-color`: Sets the background color.
- `padding`: Defines the space between the content and the element's border.
- `margin`: Sets the space outside the element's border.
- `border`: Sets the border properties.

Example:

```css
/* styles.css */

h1 {
  color: blue;
  font-size: 24px;
  background-color: yellow;
  padding: 10px;
  margin: 0;
  border: 1px solid black;
}
```

3. Applying Styles with Classes and IDs
--------------------------------------

Classes and IDs allow you to target specific elements or groups of elements for styling. They are defined in the HTML using the `class` and `id` attributes.

- Class Selector: To target elements with a specific class, prefix the class name with a dot (`.`) in your CSS code. For example:

  ```html
  <h1 class="my-heading">Hello, CSS!</h1>
  ```

  ```css
  .my-heading {
    color: blue;
    font-size: 24px;
  }
  ```

- ID Selector: To target a unique element using its ID, prefix the ID name with a hash (`#`) in your CSS code. For example:

  ```html
  <p id="my-paragraph">This is a paragraph.</p>
  ```

  ```css
  #my-paragraph {
    color: red;
  }
  ```

4. External CSS Files
---------------------

To separate your CSS code into an external file, create a file with a `.css` extension and link it in your HTML document using the `<link>` tag in the `<head>` section. For example:

```html
<head>
  <link rel="stylesheet" href="styles.css">
</head>
```

This way, you can maintain and reuse your styles across multiple HTML pages.
