HTML Basics: A Beginner's Guide
==============================

HTML (Hypertext Markup Language) is the standard markup language used to create web pages. It provides the structure and content of a webpage, defining how the elements on the page are organized and displayed. In this tutorial, we'll cover the basic elements and syntax of HTML.

1. Setting Up the HTML Document
-------------------------------

To start an HTML document, you need to create a file with a `.html` extension. You can use any text editor to write HTML code. Begin your HTML document with the following code:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Page Title</title>
</head>
<body>

</body>
</html>
```

- `<!DOCTYPE html>`: This declaration tells the browser that the document is an HTML5 document.
- `<html>`: This is the root element of an HTML page.
- `<head>`: This section contains meta information about the document, such as the title.
- `<title>`: This element sets the title of the webpage, which appears in the browser's title bar or tab.
- `<body>`: This is the main content of the webpage.

2. Adding Content to the Webpage
-------------------------------

Within the `<body>` tags, you can add various HTML elements to create the content of your webpage. Here are some commonly used elements:

- `<h1>` to `<h6>`: These elements define headings of different sizes, with `<h1>` being the largest and `<h6>` being the smallest.
- `<p>`: This element represents a paragraph of text.
- `<a>`: This element creates a hyperlink. It requires an `href` attribute to specify the destination URL.
- `<img>`: This element inserts an image into the webpage. It requires a `src` attribute that points to the image file.

Example:

```html
<body>
  <h1>Welcome to My Webpage</h1>
  <p>This is a paragraph of text.</p>
  <a href="https://www.example.com">Click here</a> to visit Example.com.
  <img src="image.jpg" alt="Description of the image">
</body>
```

3. Structuring Content with HTML Tags
------------------------------------

HTML provides a variety of tags to structure and organize content. Here are some commonly used ones:

- `<div>`: This tag is used as a container to group elements together.
- `<ul>` and `<ol>`: These tags represent unordered and ordered lists, respectively.
- `<li>`: This tag is used to define individual items within a list.
- `<table>`: This tag creates a table with rows and columns.
- `<tr>`: This tag represents a row in a table.
- `<td>`: This tag defines a cell in a table.

Example:

```html
<body>
  <h1>About Me</h1>
  <div>
    <h2>Education</h2>
    <ul>
      <li>High School</li>
      <li>College</li>
    </ul>
  </div>
  <h2>Contact</h2>
  <table>
    <tr>
      <td>Name</td>
      <td>John Doe</td>
    </tr>
    <tr>
      <td>Email</td>
      <td>john@example.com</td>
    </tr>
  </table>
</body>
```

4. Styling with CSS
-------------------

CSS (Cascading Style Sheets) is used to style HTML elements and control their appearance. You can either include CSS code within `<

style>` tags in the `<head>` section or link to an external CSS file using the `<link>` tag.

Example:

```html
<head>
  <style>
    h1 {
      color: blue;
      font-size: 24px;
    }
    p {
      font-style: italic;
    }
  </style>
</head>
<body>
  <h1>Welcome to My Webpage</h1>
  <p>This is an italicized paragraph of text.</p>
</body>
```
