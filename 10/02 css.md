To import a CSS file into your HTML document, you can use the `<link>` tag. Here's how you can do it:

1. Create a CSS file
---------------------
First, create a separate CSS file with a `.css` extension. You can use any text editor to write CSS code. For example, let's create a file named `styles.css` and save it in the same directory as your HTML file.

2. Link the CSS file to your HTML document
------------------------------------------
In the `<head>` section of your HTML document, add the following `<link>` tag to link the CSS file:

```html
<head>
  <link rel="stylesheet" href="styles.css">
</head>
```

- The `rel` attribute specifies the relationship between the HTML file and the linked resource, in this case, the CSS file. Use `stylesheet` to indicate that it's a style sheet.
- The `href` attribute specifies the path to the CSS file. In this example, `styles.css` is in the same directory as the HTML file, so you only need to provide the file name. If the CSS file is in a different directory, you need to specify the relative or absolute path accordingly.

3. Apply styles from the CSS file
---------------------------------
In your CSS file (`styles.css` in this example), you can define styles for various HTML elements. For example:

```css
/* styles.css */

body {
  font-family: Arial, sans-serif;
  background-color: #f1f1f1;
}

h1 {
  color: blue;
}

p {
  font-size: 16px;
  line-height: 1.5;
}
```

In this CSS code, we're setting the font family and background color for the `<body>` element, changing the color of `<h1>` elements to blue, and setting the font size and line height for `<p>` elements.

Save the CSS file after defining your styles.

4. Verify the CSS styles
------------------------
Now, when you open your HTML document in a web browser, it will import the CSS file, and the styles defined in the CSS file will be applied to the corresponding HTML elements.

For example, if you have the following HTML code:

```html
<body>
  <h1>Welcome to My Webpage</h1>
  <p>This is a paragraph of text.</p>
</body>
```

The `<h1>` element will appear in blue, and the `<p>` element will have a font size of 16 pixels and a line height of 1.5.

That's it! You have successfully imported a CSS file into your HTML document. Now you can easily maintain and update your styles separately in the CSS file, making your HTML code cleaner and more manageable.