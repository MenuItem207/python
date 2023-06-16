
Flexbox Basics: A Beginner's Guide
==================================

Flexbox is a CSS layout module that provides a flexible way to arrange and distribute space among elements within a container. It simplifies complex layout tasks and allows you to create responsive and flexible designs. In this tutorial, we'll cover the fundamental concepts and properties of Flexbox.

1. Understanding Flexbox Terminology
-----------------------------------

Before diving into the properties, let's familiarize ourselves with the basic terms used in Flexbox:

- Flex Container: The parent element that contains the flex items.
- Flex Items: The child elements contained within the flex container.
- Main Axis: The primary axis along which the flex items are laid out. By default, it's horizontal (left to right).
- Cross Axis: The perpendicular axis to the main axis.

2. Creating a Flex Container
---------------------------

To create a Flexbox layout, start by setting the `display` property of the parent element (the flex container) to `flex` or `inline-flex`. This activates the Flexbox behavior on the container. For example:

```css
.container {
  display: flex;
}
```

3. Aligning Flex Items along the Main Axis
------------------------------------------

Flexbox provides properties to control the alignment of flex items along the main axis. Here are a few commonly used properties:

- `justify-content`: Defines how the flex items are distributed along the main axis. Values include `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, and more.

Example:

```css
.container {
  display: flex;
  justify-content: center;
}
```

This centers the flex items horizontally within the container.

4. Aligning Flex Items along the Cross Axis
-------------------------------------------

Flexbox also offers properties to control the alignment of flex items along the cross axis. Here are a few commonly used properties:

- `align-items`: Specifies how the flex items are aligned along the cross axis. Values include `flex-start`, `flex-end`, `center`, `baseline`, and `stretch`.

Example:

```css
.container {
  display: flex;
  align-items: center;
}
```

This centers the flex items vertically within the container.

5. Controlling Flex Item Sizes and Spacing
------------------------------------------

Flexbox provides properties to control the size and spacing of flex items. Here are a few commonly used properties:

- `flex-grow`: Specifies the ability of a flex item to grow and occupy available space.
- `flex-shrink`: Determines the ability of a flex item to shrink when there is limited space.
- `flex-basis`: Sets the initial size of a flex item before it expands or shrinks.
- `flex`: A shorthand property that combines `flex-grow`, `flex-shrink`, and `flex-basis` into a single declaration.

Example:

```css
.container {
  display: flex;
}

.item {
  flex: 1;
}
```

This evenly distributes available space among the flex items by giving them equal flex grow values.

6. Creating Flexible Wrapping Layouts
------------------------------------

Flexbox allows flex items to wrap to new lines when there isn't enough space in the container. This behavior is controlled by the `flex-wrap` property.

Example:

```css
.container {
  display: flex;
  flex-wrap: wrap;
}
```

This enables flex items to wrap to the next line if there isn't enough space horizontally.

