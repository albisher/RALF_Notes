Obsidian Cheat Sheet
from https://publish.obsidian.md/orbnetsys/z_template/Obsidian+Cheat+Sheet


Heading 1

# Heading 1

Heading 2

## Heading 2

Heading up to six

# This is a heading 1
## This is a heading 2
### This is a heading 3
#### This is a heading 4
##### This is a heading 5
###### This is a heading 6

Italic

*text*

Bold

**text**

Italic Bold*

***text***

Strikethrough

~~this text is crossed out~~

Grey Highlight

`Highlight`

Grey Highlight Bold

**`Grey Highlight Bold`**

Highlight

==this text is highlighted==

Code Blocks

Put 3 (```) signs before and after the code.

```
<code>

```

Code Blocks - Code Language

Put 3 (```) signs before with the language name then and (```) after the code.

html

<!DOCTYPE html>  
<html>  
<head>  
<title>My First Web Page</title>  
</head>  
<body>  
<h1>Hello, World!</h1>  
<p>This is my first paragraph.</p>  
<img src="image.jpg" alt="My Image">  
</body>  
</html>

csharp

using System;

namespace HelloWorld
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("Hello World!");    
    }
  }
}

URL Link
https://google.co.uk/

https://google.co.uk/

Named URL Link
Google UK


[Google UK](https://google.co.uk/)

Line Break

---

Bullet

    Bullet Point 1
    Bullet Point 2

- Bullet 

Checklist

    Checklist unticked
    Checklist ticked

- [ ] list 
- [x] list 

Blockquotes

    Blockquotes

        Blockquotes Block

            Blockquotes Block Block

     Blockquote Tab

         Blockquotes Block Tab

             Blockquotes Block Block Tab

> Blockquotes
>> Blockquotes
>>> Block Block

> 	 Blockquote Tab
>> 	 Blockquotes Block Tab
>>> 	 Blockquotes Block Block Tab

Quote

 Quote
	Quote Tab
		Quote Tab

	 Quote
		Quote Tab
			Quote Tab

Callouts

> [!info] 
> Here's a callout block. 
> It supports **Markdown**, [[Internal link|Wikilinks]], and [[Embed files|embeds]]!
> 
> ![[z_img/ce9088d7c8331f747aaba60bb28d6735_MD5.jpg|135]]

Info

Here's a callout block.
It supports Markdown, Wikilinks, and embeds!

z_img/ce9088d7c8331f747aaba60bb28d6735_MD5.jpg

> [!tip] Callouts can have custom titles
> Like this one.

Callouts can have custom titles

Like this one.

> [!faq]- Are callouts foldable? > Yes! In a foldable callout, the contents are hidden when the callout is collapsed.

// Use `-` to default closed, use `+` to default open.

Are callouts foldable?
Are callouts foldable?

Yes! In a foldable callout, the contents are hidden when the callout is collapsed.

    Callout types

Info
Tip
Warning
Todo
Example
Abstract
Question
Success
Quote
Failure
Danger
Bug

[https://help.obsidian.md/callouts#Customize+callouts](Obsidian - Customize Callouts with CSS)
Tables

Right click Insert > Table
Table Cell A 	Table Cell B
A 	B


| Table Cell A | Table Cell B |
| ------------ | ------------ |
| A            | B            |

Table with images.
Table Cell A 	Table Cell B
z_img/7204fc7d6cced938b154dbacb8c013e7_MD5.jpeg 	z_img/ce9088d7c8331f747aaba60bb28d6735_MD5.jpg


| Table Cell A                                              | Table Cell B                                             |
| --------------------------------------------------------- | -------------------------------------------------------- |
| ![[z_img/7204fc7d6cced938b154dbacb8c013e7_MD5.jpeg\|140]] | ![[z_img/ce9088d7c8331f747aaba60bb28d6735_MD5.jpg\|135]] |

Emojis

Emojis are valid, in Windows press [Windows] + [.] from the icon menu select the icon you want to use.

😀😁😂🤣😃😄😅😆😉😊😋😎 👈👉☝️🫵👆👇✌️🤞🫰🖖🫱🫲 ▶️⏸️⏯️⏹️⏺️⏭️⏮️⏩⏪◀️🔼⏫
Images

![[z_img/ce9088d7c8331f747aaba60bb28d6735_MD5.jpg]]
![[z_img/ce9088d7c8331f747aaba60bb28d6735_MD5.jpg|175]]
![[z_img/ce9088d7c8331f747aaba60bb28d6735_MD5.jpg|135]]

\\\ Drag an drop into canvas
\\\ link|width (Height auto)

z_img/ce9088d7c8331f747aaba60bb28d6735_MD5.jpg

z_img/ce9088d7c8331f747aaba60bb28d6735_MD5.jpg

z_img/ce9088d7c8331f747aaba60bb28d6735_MD5.jpg
GIF

z_img/d8f7034089e8157e0c7203a599d8aea1_MD5.gif
Videos
YouTube

For this the direct link has been copied, no embed required.

![](https://www.youtube.com/watch?v=jjmaRlubLD0)
![](https://www.youtube.com/embed/jjmaRlubLD0?si=yTmXZzoHdvDyDT84)

\\\ YouTube full page link or embed link both work.

Vimeo

/// Share: Embed

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/347119375?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Sample Video"></iframe>
</div>

 \\\ This part is not required.
\\\ <script src="https://player.vimeo.com/api/player.js"></script>

Local Video

![[z_img/d5ce356d6bf07f6b5f1deeac70f85df5_MD5.mp4]]

/// Local video, drag a drop video into canvas

Obsidian Links
Link to other document in vault.

Right click Add Link start typing the name of the other document.

ORBNET Systems Products

Same link different text

[[ORBNET Systems Products]]

[[ORBNET Systems Products|Same link different text]]

Link to headings in same document

Right click Add Link then start with # then start typing the name of the other heading you want to link to.

Heading 1

Heading 1 is the link

[[#Heading 1]]

[[#Heading 1|Heading 1 is the link]]

