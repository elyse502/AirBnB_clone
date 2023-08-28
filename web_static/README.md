# Concepts
_For this project, we expect you to look at these concepts:_
* [HTML/CSS](https://intranet.alxswe.com/concepts/2)
* [The trinity of front-end quality](https://intranet.alxswe.com/concepts/4)

## 1. HTML/CSS
Open web technologies (such as HTML and CSS) have three most peculiar particularities compared to other technologies:
* Because anyone is meant to be allowed to code an interpreter for those languages (that what browsers are!), people making decisions on those technologies are part of an open consortium of companies (called the W3C), which operates on consensus; therefore they evolve rather slowly.
* Reverse compatibility is among the most important values kept in mind when deciding on evolutions, because newest browsers should keep being able to run older websites, and older browsers should be able to access newest websites.
* They were not initially designed to make applications or well-designed pages, but just display research documents; while they have come a long way since then, it is visible in the ways things are done.
For each of those three reasons, it is quite important, in order to understand what those technologies are made of today, to understand where they come from, and the legacy that comes with them.

## At first, there was HTML
### A bit of history
HTML and HTTP, the earliest bricks of the web (which he initially called World Wide Web), were invented by sir Tim Berners-Lee when he was working for the CERN in France/Switzerland. (Since the lab is on the border, which country the web was actually invented in is still to this day a controversial topic; also, he is an English citizen, so here is more controversy!)

At that point, the internet was already open to the public, but lacked a common software platform, and this was Berners-Lee’s attempt to bring one to the world.

### The difference between the internet and the web?
The web is anything that happens in your browser. When you’re using Skype, you’re using the internet and not the web.

What were people using the internet for before the web: for instance, emails (but not in a browser like Gmail, only with a mail client like Outlook/Thunderbird/Apple’s Mail today), newsgroups (something that still exists but is not mainstream to this day, and feels a bit like today’s forums), …

The problem was: all of those (Skype, emails, …) use their own way to structure the data they send. It would make it very disorganized to make something available somewhere on the internet, like the research papers of Berners-Lees colleagues at the CERN.

So, he came up with two things:
* HTTP, a protocol defining how servers and clients can organize their communications together. It is so synonymous to the web, that what we call software web servers today (Apache, nginx, …) are technically HTTP servers, i.e. servers designed to receive HTTP requests and send back appropriate responses following the protocol.
* HTML, a markup language to help structure the research papers: what is a title, what is a paragraph, etc.
On Christmas in 1990, he put the first web server online, and published the very first web client in a newsgroup, so that people could go see his website. The web was born.

At this point, the need for such a technological stack to make material available online was so obvious, that Berners-Lee was by far not the only one to come up with such an idea. The main difference was that unlike the other proposals, Berners-Lee’s World Wide Web was free and available for all to use. As he famously said: “This is for everyone”.

![this_is_for_everyone](https://github.com/elyse502/AirBnB_clone/assets/125453474/aca00c4b-62ca-4788-8851-1cc982339830)

_Tim Berners-Lee was invited to appear on stage during the gigantic opening event for the London Olympics. He was simply sitting at a NeXT computer, just like the one he used to host his first web server, in front of his famous quote._

Industry vendors started to want to use his protocol, so instead of keeping a tight grip on it, he created the World Wide Web Consortium (W3C) in 1994, which company pay a membership to in order to be able to help making the decisions to push those technologies forward. Berners-Lee is still the head of the W3C to this day.

## In a nutshell
### HTML in a nutshell
HTML is a markup language, which you are expected to be acquainted with from your level 2 project. If you feel like you need a mind-refresher, feel free to check out some tutorials, such as this one: [http://learn.shayhowe.com/html-css/](https://learn.shayhowe.com/html-css/)

The breadth of HTML is actually not very large, as it is not meant to include advanced features; getting acquainted on each relevant tag and attribute doesn’t take much time, because there aren’t that many. The part of HTML that is trickiest to go over is probably forms, because there are quite a few possible components (text fields, checkboxes, text areas, … even sliders and color pickers in the most recent HTML specifications!)

The promise of HTML is that you should keep your document as properly structured and semantic as you can; and if you do, it should remain easily accessible to the browsers that will exist in 20 years, while also making it easier to keep your code accessible, performant, and optimized for search engines through time. See: [http://vanseodesign.com/web-design/semantic-html/](http://vanseodesign.com/web-design/semantic-html/)

### CSS in a nutshell
CSS (Cascading Style Sheets) were invented by Bert Bos and Håkon Wium Lie, because HTML was getting less and less semantic, and more and more about presentation, which would make it less future-proof and more verbose.

For instance, you could write that:
`<center><p><font color="red">Hello to <b>all</b> of my visitors!</font></p></center>`
The fact that a text should be centered, have a certain color, and be represented in bold is part of presentation, and shouldn’t be in the HTML. The fact that it’s a paragraph, however, is part of the structure, and therefore is semantic information.
Also, if you needed to make a whole page red, you needed to write `<font color="red">` at every single line.

CSS enforces not only semantics in the HTML, but also mutualization of the presentation layer, and therefore less code.

Now, `<center>`, `<font>` and `<b>` are banned in HTML, and we got some more semantic tags, like `<strong>`, `<em>`, and more recently, `<article>`, `<section>`, `<aside>`, …

Wondering about the difference between `<strong>` and `<b>`? –> [http://www.html-5-tutorial.com/strong-and-b-elements.htm](http://www.html-5-tutorial.com/strong-and-b-elements.htm)

## Web development tools
Before diving into your first front-end development project, you should take some time to learn to use the web development tools that are embedded into all modern browsers. Search online how to access the ones for the browser you wish to be using.

Those tools are typically more powerful than just for HTML/CSS development, and also cover JavaScript debugging, tracking HTTP requests, even some performance diagnostic tools sometimes. The HTML/CSS pane usually displays the HTML code as the browser interprets it, on the left (as a tree that you can deploy or fold back), and the CSS rules to the right, which you can edit in place. Of course, all of the edits you’re doing in there are being done in the browser’s memory. If you want to keep these changes, you’ll have to do them in your source code.

![browser_tool](https://github.com/elyse502/AirBnB_clone/assets/125453474/c3cc21e3-67c9-4b4a-a2e7-5d2d4c5d1055)

## Block or inline? Absolute or relative?
One key notion to CSS is in the difference between the `block` and `inline` values to the `display` statement, and also `inline-block`. The most basic `display` values:
* `none`, hides the HTML element.
* `block` means it will be fluid (take up the entire width of the browser’s window) and will stack up vertically (top to bottom). It is the default behavior of `<p>`, `<ul>`, `<li>`, `<h1>`, `<div>` … You can add margins and paddings to those.
* `inline` means it will be inside the textual flow of the block. It is the default behavior of `<a>`, `<strong>`, `<em>`, `<img>`, `<span>`, … You can not add margins and paddings to those.
* `inline-block` is a mix of both: the element will be inside the textual flow of the block, but it will also accept margins, paddings, …

Another key notion is the `position` statement:
* `static` is the one by default, so you’ll rarely have to explicit it. An element is positioned where it is expected that it should be.
* `relative` will help you position the element relatively to its expected position, for instance 2px higher, or 5px to the left, etc.
* `absolute` will remove the element from the flow of the page, and position it relatively to another block, most often the entire page. For instance, before you change anything else, it will often be at the top left of the page, “flying ” over the rest of your HTML document.
* `fixed` will do the same thing as `absolute`, but will behave differently when you scroll up or down: absolute elements will scroll with the rest of the page, while fixed ones won’t, and will stay right at the same spot in front of you. More about positions here: [http://www.w3schools.com/css/css_positioning.asp](https://www.w3schools.com/css/css_positioning.asp)

## CSS Layouts
Because CSS was never meant to be to do complex layouts, but was meant for “flat” documents, CSS layout went through a bit of history.

### Tables and images
Initially, web designers and brands wanted websites to offer “pixel-perfect” like on print. However, this was very difficult to achieve as CSS did not render similarly across browsers, and fonts rendered very differently depending on the OS (which is still the case today, actually). Therefore, the very first “visual” websites were mostly images ordered together in border-less tables. This was obviously a nightmare in performance (huge images + very verbose HTML did not fare well with slow web connections) and in accessibility/SEO (tables are meant for tabular data and are recognized as such semantically, and texts in images were not recognized at text; for instance, they couldn’t be copy-pasted).

HTML frames were also very used at the time, but they fell out of fashion for those same reasons: performance because you’re loading many webpages instead of one, accessibility because it was near impossible to navigate the user from one frame to the other (with the keyboard, for instance), SEO because the URL of a webpage didn’t change when navigating, so some composite pages didn’t even have a navigable URL.

## Early web standards
In the late 90s, a group of web developers and designers (most of them were a bit of both) started to evangelize about how it was entirely possible to make built great websites entirely with standards. The “Standard Web Project” was created in 1998 by Jeffrey Zeldman, who subsequently wrote his breakthrough book “Designing with Web Standards”. The book was a list of practical tricks to get each browsers to do what you need them to do.

Keep in mind that each browser still had a very, very different interpretation of CSS back then, so you basically had to develop one CSS per browser. Eventually, browser got more mature, and most code could gradually be mutualized for all browsers. Today, websites that don’t leverage the web standards are very rare.

Some key links from that time:
* The Dao of Web Design is an article written in 2000 on A List Apart, the blog Jeffrey Zeldman founded for front-end experts to share their tricks. While most articles from back then have aged pretty badly, since browsers changed so much over the last few years, this one is still very current. It teaches people to let go of pixel-perfect, in order to embrace the goodies contained in web standards. Read it here: [http://alistapart.com/article/dao](https://alistapart.com/article/dao/)
* CSS Zen Garden was created by Dave Shea to showcase what CSS can do. It is basically a single HTML file, on which any one can contribute an original CSS stylesheet, to make it do interesting things. Check it out here: [http://www.csszengarden.com](http://www.csszengarden.com/)

## Float layout
As we’ve discussed, natively, HTML stacks fluid blocks vertically. People wanted to stack blocks horizontally too (next to each other), but except for positioning them as absolute (which breaks the flow of the page), the only other way to do it was to make them “float”.

The `float` statement, which takes `left` or `right` (or the default value `none`) was designed to make medias (like images) float the left or right of the text; and the text would nicely “go around” the image. But people found ways to “abuse” the `float` statement in order to build complex layouts. The `clear` statement is `float`‘s antagonist: it makes an element avoid to float by its previous elements.

More about `float` and `clear`: http://www.w3schools.com/css/css_float.asp

Because more recent options are not entirely mature yet, a lot of websites are still being made with floating layout.

## CSS Display Table
It took long years for the W3C to have consensus on some layout specifications, and display table is one of the first ones that made it maturity. The idea is to take some HTML that doesn’t contain the `<table>` element, but make it behave like tables just with CSS.
It had been moderately popular, but it never rose to widespread uses, because one could not manage every layout use case this way.

## CSS Flexbox
As a far more powerful alternative to CSS Display Table, CSS Flexbox has huge support from the browsers and the industry, despite the implementations in browsers not being 100% consistent in all cases. Many websites and web applications in the industry use CSS Flexbox: some mentors working at Salesforce confirmed that all applications are now built using it; another mentor working on Google Photos confirmed that it is what is being used there too. And for widespread adoption, the most used CSS frameworks are now switching to Flexbox, one by one.

Here is an excellent and fun tutorial for learning Flexbox: http://flexboxfroggy.com

## The other ones?
Other CSS layout specifications are in the work at the W3C, such as CSS Grid; but none of them seem near maturity at all at this point. And it can be argued that the support CSS Flexbox is getting could actually be detrimental to them, since the industry seems gradually happy with it.

## CSS Media Queries and Responsive Web Design
Another recent interesting piece of recent CSS history is the introduction of the CSS Media Queries, and the concept of Responsive Web Design.

Media queries allow to express that certain CSS rules should only be executed when certain conditions are in place (such as based on the screen’s resolution, or the number of colors a graphics card can handle). But the one condition that started to get very used, is the one allowing to only execute some CSS depending on the browser’s width. As you may have understood, this allows a single CSS codebase for a website regardless of the size of the browser, enabling and disabling some CSS rules when it passes certain width thresholds.

Do you remember Jeffrey Zeldman? (He’s the guy who founded A List Apart, the Web Standards Project, and wrote Designing with Web Standards) He’s part of the people who actually came up with the notion of Responsive Web Design, the idea to use media queries to make a single website adapt depending on the browser’s width.

## Media query syntax
It looks like this:
```
@media screen and (min-width:600px) {
  nav {
    float: left;
    width: 25%;
  }
  section {
    margin-left: 25%;
  }
}
```
The above CSS rules will only apply when the browser displays the webpage on a screen (as opposed to printed on paper, for instance), and the browser’s window is at least 600px wide.

More about media queries: http://www.w3schools.com/css/css_rwd_mediaqueries.asp

## Viewport
Feature phones (the things that came before smartphones) didn’t “zoom pages out” when displaying a non-mobile webpage so that you could see the whole page; you would simply see a corner of the webpage that was the size of your phone’s screen, and had to swipe around to see the rest.
When Apple introduced the iPhone in 2007, it introduced the notion of viewport: the width of the phone would, by default, not be displaying the same small width of the webpage; it would display 1024px on a device that really is 320px wide. Instead of swiping around to see each bit of the webpage, you would have to zoom in to read texts. Soon, all other smartphones adopted the same behavior.
The way to describe it is: although the screen is 320px wide, its viewport (what it really displays of a webpage) is 1024px wide.

But this would create problems with responsive websites, as you actively want them to display the real width of the screen. Therefore, Apple introduced a HTML tag to override the viewport the browser, which all other browsers implemented later too. This is what developers typically set it as for fluid designs such as responsive web designs:
```
<meta name="viewport" content="width=device-width, initial-scale=1">
```
More about the viewport: https://developer.mozilla.org/en-US/docs/Mozilla/Mobile/Viewport_meta_tag

## Some links
* Many of the CSS concepts on this page are introduced and demoed on this very visual and well-polished website: http://learnlayout.com
* “Like the CSS spec, but readable”, according to Kaelig (one of your mentors who is a front-end engineer at Salesforce): http://book.mixu.net/css/

# 2. The trinity of front-end quality
Have you noticed that this concept does not contain any link? By now, you should be able to find your own sources, based on the proper technical terms we’ll keep giving you in the concepts, usually introduced in bold font.

When talking about front-end quality, there are 3 main end goals that front-end developers keep striving for:
* Accessibility
* Performance
* SEO

## SEO
**SEO (Search Engine Optimization)** refers to making sure your website is ranked relevantly high on search engines’s SERPs , like Google’s.

Because the exact rules checked by search engines are not entirely public, and competition for popular queries is so fierce, SEO is often referred to as black magic… and well, sometimes it does feel like it is! But there are very clear best practices to apply to be respected and taken seriously by Google and its friends.

Of course, making your markup as semantic as you can will help the search engine understand your webpage; but by now, most websites do that right, so it is definitely not going to be enough.

More current strategies involve the content you put in your website, the URLs, the internal and/or external linking, the website’s performance, … The list of things that can be done to improve one’s SEO is endless!

To monitor SEO results, people usually use monitoring tools, which are going to keep track of search engine rankings continuously for them in various countries. Most of those tools are paid, but you’ll find a few free ones with the most limited features. Many of those tools also meant to help define the right SEO strategy in the first place, when you try to figure out which queries you should be optimizing for (a step called keyword research ). For instance, if the tool tells you that a query doesn’t involve many competitors fighting for it, and yet Google Trends tells you it is a query that is heavily being ran by Google users, then you might be sitting on a goldmine!

Another important note to keep in mind is that a SEO strategy will of course contain the **targeted queries** of someone actively looking for you (for instance, Safeway probably works hard to be ranked high on the “safeway” query), but also the untargeted queries of someone who is not specifically looking for you, but whose attention you seek (for instance, Safeway probably works even harder to be ranked high on the “san francisco grocery store” query, or one even more competitive: just “grocery store”, if it’s relevant for them). Deciding which queries make sense to pursue is a critical component of SEO strategy.

## Accessibility
Stéphane Deschamps is a mentor and a hardcore internationally recognized web accessibility expert. He once told me the story of how he starts his accessibility training sessions.

First thing: he’d start by asking everyone to stand up. Then he’d ask people wearing glasses to sit down; then people who had back pain sometimes; then people who already had had a broken arm; etc. At the end of his list, he’d tell the people still standing that they could ignore the next few hours, because they will be about all of the other people in the room. The catch is that by then, there would only be at most one person standing, most often none. He now had the room’s attention.

In real life, it is estimated that a website may lose as high as 15% of its visitors to bad accessibility. Think: someone with poor eyesight who couldn’t read the menu button properly because of their low contrast, and gave up; or someone who worked hard with their hands today, and can’t handle the mouse anymore to fill in a long form, and the keyboard navigation won’t work, etc.

Having a semantic and valid HTML markup will already go a long way to make one’s website accessible; but it is definitely not enough, and issues are hidden in the details (images, colors, …).

Also, for complex applications for which you feel like some bits of the page should be more explicit in their purpose, you can give that extra information with WAI-ARIA  (often referred to as just “ARIA”).

## The specific case of network fault-tolerance
Another kind of loss of accessibility is when resources (such as CSS files, images, JavaScript files) are inaccessible, such as for network reasons. Without CSS, without JavaScript, without images, your website should still work. It may not have as much styling and interactivity, but people must still be able to post that micro-blogging status, for instance.

Browsers often have built-in tools (or plugins) that allow you to see your website without images, without CSS, without JS, …

## Front-end performance
Did you know that over 90% of the time spent by a user waiting for your webpage is happening in the front-end, rather than the back-end? The reasons are pretty obvious when you think about it: you can host your code on faster servers, or scale it on a higher number of them; but there’s nothing you can do to make the user’s browser environment better. To ensure all browsers can interpret it, you have to send your user code that respects web standards (which are sometimes verbose), and you can’t make that code smaller than the standards allow. It has to go through the network, be entirely loaded and run by the browser, you can’t have the browser “preload” anything. Well, actually…

There are many pitfalls and tricks to address web performance. All ways attempt to either make each file smaller, or to lower the number of files (it is magnitudes more expensive to download two files of 50kB each, than one file of 100kB).

Some pitfalls:
* Forgetting to enable GZip and set Cache expirations on your web server’s configuration
* Using many external JS libraries, including some you absolutely didn’t need
* Using huge images displayed smaller
* Leaving the metadata in your images
* Etc…

Some tricks:
* Images sprites
* No CSS or JS inside the HTML (.js and .css files will be cached on first call, won’t have to be downloaded next time).
* Ajax calls that can be done with GET HTTP verb should use it (that way, they are cached)
* CSS and JS files are concatenated into one single file each
* CSS and JS files are “minified”
* Images are recompressed

As usual with quality, you will want to measure. But there are many ways to measure a front-end’s load time. Should it be the **Time To First Byte**? **Page Load Time**? **Time To First Paint**? You should define your strategy, and monitor the measures you feel are relevant.

Typically, the way measures are done is:
* The cache is cleared, the page is loaded, and the measurements are noted. The operation is done 3 times. If one is very significantly apart to the others, it is removed, to account for potential network issues unrelated to the website. The final result is the average of remaining calls.
* The page is loaded without clearing the cache, and the measurements noted. Again, 3 times, removing very significantly wrong measures, and the final result is the average. How to measure, you say? Just use the performance measuring tools that are likely to be in your browser.

 _This is Google Chrome’s diagnostic of the stackoverflow.com website, with cache cleared. As you can see, the back-end performance of generating the HTML page is 180ms (actually way less, if you remove the round-trip the data is doing) out of 1.30s to finish. Load time is 1.11s, which is not too bad!_

# Background Context
## Web static, what?
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:
* Create simple HTML static pages
* Style guide
* Fake contents
* No Javascript
* No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Before starting, please fork or clone the repository `AirBnB_clone` from your partner if you were not the owner of the previous project.

# Resources🏗️
### Read or watch:
* [Learn to Code HTML & CSS](https://learn.shayhowe.com/html-css/) (_until “Creating Lists” included_)
* [Inline Styles in HTML](https://www.codecademy.com/article/html-inline-styles)
* [Specifics on CSS Specificity](https://css-tricks.com/specifics-on-css-specificity/)
* [CSS SpeciFishity](https://www.standardista.com/cgi-sys/suspendedpage.cgi)
* [Introduction to HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
* [MDN](https://developer.mozilla.org/en-US/)
* [center boxes](https://css-tricks.com/centering-css-complete-guide/)

# General
* What is HTML
* How to create an HTML page
* What is a markup language
* What is the DOM
* What is an element / tag
* What is an attribute
* How does the browser load a webpage
* What is CSS
* How to add style to an element
* What is a class
* What is a selector
* How to compute CSS Specificity Value
* What are Box properties in CSS

# Requirements
## General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be W3C compliant and validate with [W3C-Validator](https://github.com/alx-tools/W3C-Validator)
* All your CSS files should be in `styles` folder
* All your images should be in `images` folder
* You are not allowed to use `!important` and `id` (`#...` in the CSS file)
* You are not allowed to use tags `img`, `embed` and `iframe`
* You are not allowed to use Javascript
* Current screenshots have been done on `Chrome 56` or more.
* No cross browsers
* You have to follow all requirements but some `margin`/`padding` are missing - you should try to fit as much as you can to screenshots

# More Info

![hbnb_step1](https://github.com/elyse502/AirBnB_clone/assets/125453474/4b8e54fb-5e71-4968-825d-79300962387f)

# Tasks📃
## 0. Inline styling: [0-index.html](0-index.html)
An HTML page that displays a header and a footer.

Layout:
* Body:
  * no margin
  * no padding
* Header:
  * color #FF0000 (red)
  * height: 70px
  * width: 100%
* Footer:
  * color #00FF00 (green)
  * height: 60px
  * width: 100%
  * text `Best School` center vertically and horizontally
  * always at the bottom at the page

Requirements:
* You must use the `header` and `footer` tags
* You are not allowed to import any files
* You are not allowed to use the `style` tag in the `head` tag
* Use inline styling for all your tags

<img width="2160" alt="98f4ac1b0644512ce7ae91a9e8e61e8fe174911d" src="https://github.com/elyse502/AirBnB_clone/assets/125453474/868930eb-362d-493f-8548-24c7f130de90">

## 1. Head styling: [1-index.html](1-index.html)
An HTML page that displays a header and a footer by using the `style` tag in the `head` tag (same as `0-index.html`)

Requirements:
* You must use the `header` and `footer` tags
* You are not allowed to import any files
* No inline styling
* You must use the `style` tag in the `head` tag

The layout must be exactly the same as `0-index.html`

## 2. CSS files: [2-index.html](2-index.html), [styles/2-common.css](styles/2-common.css), [styles/2-header.css](styles/2-header.css), [styles/2-footer.css](styles/2-footer.css)
An n HTML page that displays a header and a footer by using CSS files (same as `1-index.html`)

Requirements:
* You must use the `header` and `footer` tags
* No inline styling
* You must have 3 CSS files:
  * `styles/2-common.css`: for global style (i.e. the `body` style)
  * `styles/2-header.css`: for header style
  * `styles/2-footer.css`: for footer style

The layout must be exactly the same as `1-index.html`

## 3. Zoning done!: [3-index.html](3-index.html), [styles/3-common.css](styles/3-common.css), [styles/3-header.css](styles/3-header.css), [styles/3-footer.css](styles/3-footer.css), [images/](images/)
An HTML page that displays a header and footer by using CSS files (same as `2-index.html`)

Layout:
* Common:
  * no margin
  * no padding
  * font color: #484848
  * font size: 14px
  * font family: `Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;`
  * [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon.png) in the browser tab
* Header:
  * color: white
  * height: 70px
  * width: 100%
  * border bottom 1px #CCCCCC
  * [logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/logo.png) align on left and center vertically (20px space at the left)
* Footer:
  * color white
  * height: 60px
  * width: 100%
  * border top 1px #CCCCCC
  * text `Best School` center vertically and horizontally
  * always at the bottom at the page

Requirements:
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 3 CSS files:
  * `styles/3-common.css`: for the global style (i.e `body` style)
  * `styles/3-header.css`: for the header style
  * `styles/3-footer.css`: for the footer style

<img width="2160" alt="2be1eda05a0d9097c210f2d3482a59aa858c5711" src="https://github.com/elyse502/AirBnB_clone/assets/125453474/b1313ef7-d7f8-44af-947a-c7e80a71f5da">

## 4. Search!: [4-index.html](4-index.html), [styles/4-common.css](styles/4-common.css), [styles/3-header.css](styles/3-header.css), [styles/3-footer.css](styles/3-footer.css), [styles/4-filters.css](styles/4-filters.css), [images/](images/)
An HTML page that displays a header, footer and a filters box with a search button.

Layout: (based on 3-index.html)
* Container:
  * between `header` and `footer` tags, add a `div`:
      * classname: `container`
      * max width 1000px
      * margin top and bottom 30px - it should be 30px under the bottom of the `header` (screenshot)
      * center horizontally
* Filter section:
  * tag `section`
  * classname filters
  * inside the `.container`
  * color white
  * height: 70px
  * width: 100% of the container
  * border 1px #DDDDDD with radius 4px
* Button search:
  * tag `button`
  * text `Search`
  * font size: 18px
  * inside the section filters
  * background color #FF5A5F
  * text color #FFFFFF
  * height: 48px
  * width: 20% of the section filters
  * no borders
  * border radius: 4px
  * center vertically and at 30px of the right border
  * change opacity to 90% when the mouse is on the button

Requirements:
* You must use: `header`, `footer`, `section`, `button` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 4 CSS files:
  * `styles/4-common.css`: for the global style (`body` and `.container` styles)
  * `styles/3-header.css`: for the header style
  * `styles/3-footer.css`: for the footer style
  * `styles/4-filters.css`: for the filters style
* `4-index.htm` **won’t be W3C valid**, don’t worry, it’s temporary

<img width="2160" alt="f959154b0cdf1cdf71ddef04e3787ef28462793e" src="https://github.com/elyse502/AirBnB_clone/assets/125453474/9c60c3ba-de6f-4f5c-b3b2-c8f59ecf1c33">

## 5. More filters: [5-index.html](5-index.html), [styles/4-common.css](styles/4-common.css), [styles/3-header.css](styles/3-header.css), [styles/3-footer.css](styles/3-footer.css), [styles/5-filters.css](styles/5-filters.css), [images/](images/)
An HTML page that displays a header, footer and a filters box.

Layout: (based on `4-index.html`)
* Locations and Amenities filters:
  * tag: `div`
  * classname: locations for `location` tag and `amenities` for the other
  * inside the section filters (same level as the `button` Search)
  * height: 100% of the section filters
  * width: 25% of the section filters
  * border right #DDDDDD 1px only for the first left filter
  * contains a title:
      * tag: `h3`
      * font weight: 600
      * text `States` or `Amenities`
  * contains a subtitle:
      * tag: `h4`
      * font weight: 400
      * font size: 14px
      * text with fake contents

Requirements:
* You must use: `header`, `footer`, `section`, `button`, `h3`, `h4` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 4 CSS files:
    * `styles/4-common.css`: for the global style (`body` and `.container` styles)
    * `styles/3-header.css`: for the header style
    * `styles/3-footer.css`: for the footer style
    * `styles/5-filters.css`: for the filters style

<img width="2160" alt="85bfa50b96c2985723daa75b5e22f75ef16e2b2e" src="https://github.com/elyse502/AirBnB_clone/assets/125453474/bb78f403-2f99-4c53-8f5a-530754f87392">

## 6. It's (h)over: [6-index.html](6-index.html), [styles/4-common.css](styles/4-common.css), [styles/3-header.css](styles/3-header.css), [styles/3-footer.css](styles/3-footer.css), [styles/6-filters.css](styles/6-filters.css), [images/](images/)
An HTML page that displays a header, footer and a filters box with dropdown.

Layout: (based on `5-index.html`)
* Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter `div`:
  * tag `ul`
  * classname `popover`
  * text should be fake now
  * inside each `div`
  * not displayed by default
  * color #FAFAFA
  * width same as the `div` filter
  * border #DDDDDD 1px with border radius 4px
  * no list display
  * Location filter has 2 levels of `ul`/`li`:
    * state -> cities
    * state name must be display in a `h2` tag (font size 16px)

Requirements:
* You must use: `header`, `footer`, `section`, `button`, `h3`, `h4`, `ul`, `li` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 4 CSS files:
    * `styles/4-common.css`: for the global style (`body` and `.container` styles)
    * `styles/3-header.css`: for the header style
    * `styles/3-footer.css`: for the footer style
    * `styles/6-filters.css`: for the filters style

<img width="2160" alt="6262f13624dca23ca19db505c44f88faddb82ebb" src="https://github.com/elyse502/AirBnB_clone/assets/125453474/b0ac0582-9270-4e18-92e5-b87cde13b623">

<img width="2160" alt="6e6bdfa13fa88a5f439d9e2b1dade826dd95529b" src="https://github.com/elyse502/AirBnB_clone/assets/125453474/7ce1d2a8-8fb7-43c8-be03-43ee87181f79">

## 7. Display results: [7-index.html](7-index.html), [styles/4-common.css](styles/4-common.css), [styles/3-header.css](styles/3-header.css), [styles/3-footer.css](styles/3-footer.css), [styles/6-filters.css](styles/6-filters.css), [styles/7-places.css](styles/7-places.css), [images/](images/)
An HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on `6-index.html`)
* Add Places section:
  * tag: `section`
  * classname: `places`
  * same level as the filters section, inside `.container`
  * contains a title:
      * tag: `h1`
      * text: `Places`
      * align in the top left
      * font size: 30px
  * contains multiple “Places” as listing (horizontal or vertical) describe by:
      * tag: `article`
      * width: 390px
      * padding and margin 20px
      * border #FF5A5F 1px with radius 4px
      * contains the place name:
          * tag: `h2`
          * font size: 30px
          * center horizontally

Requirements:
* You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2` `h3`, `h4`, `ul`, `li` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 5 CSS files:
    * `styles/4-common.css`: for the global style (`body` and `.container` styles)
    * `styles/3-header.css`: for the header style
    * `styles/3-footer.css`: for the footer style
    * `styles/6-filters.css`: for the filters style
    * `styles/7-places.css`: for the places style

<img width="2160" alt="bca4d17fbe21a58b66a9d5d6b85df4801d147dd0" src="https://github.com/elyse502/AirBnB_clone/assets/125453474/1dc61beb-d910-4337-b27f-dce3fd7edb65">

## 8. More details: [8-index.html](8-index.html), [styles/4-common.css](styles/4-common.css), [styles/3-header.css](styles/3-header.css), [styles/3-footer.css](styles/3-footer.css), [styles/6-filters.css](styles/6-filters.css), [styles/8-places.css](styles/8-places.css), [images/](images/)
An HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.

Layout: (based on `7-index.html`)

Add more information to a Place article:
* Price by night:
  * tag: `div`
  * classname: `price_by_night`
  * same level as the place name
  * font color: #FF5A5F
  * border: #FF5A5F 4px rounded
  * min width: 60px
  * height: 60px
  * font size: 30px
  * align: the top right (with space)
* Information section:
  * tag: `div`
  * classname: `information`
  * height: 80px
  * border: top and bottom #DDDDDD 1px
  * contains (align vertically):
      * Number of guests:
          * tag: `div`
          * classname: `max_guest`
          * width: 100px
          * fake text
          * [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_group.png)
      * Number of bedrooms:
          * tag: `div`
          * classname: `number_rooms`
          * width: 100px
          * fake text
          * [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bed.png)
      * Number of bathrooms:
          * tag: `div`
          * classname: `number_bathrooms`
          * width: 100px
          * fake text
          * [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bath.png)
* User section:
  * tag: `div`
  * classname: `user`
  * text `Owner: <fake text>`
  * `Owner` text should be in bold
* Description section:
  * tag: `div`
  * classname: `description`

Requirements:
* You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2` `h3`, `h4`, `ul`, `li` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 5 CSS files:
    * `styles/4-common.css`: for the global style (`body` and `.container` styles)
    * `styles/3-header.css`: for the header style
    * `styles/3-footer.css`: for the footer style
    * `styles/6-filters.css`: for the filters style
    * `styles/7-places.css`: for the places style

<img width="1604" alt="f4b2d4ef94bd3a2e7e1ddefa81236595686d270e" src="https://github.com/elyse502/AirBnB_clone/assets/125453474/98a1db79-51ce-4096-9b4e-747c05da5bac">

## 9. Full details: [100-index.html](100-index.html), [styles/4-common.css](styles/4-common.css), [styles/3-header.css](styles/3-header.css), [styles/3-footer.css](styles/3-footer.css), [styles/6-filters.css](styles/6-filters.css), [styles/100-places.css](styles/100-places.css), [images/](images/)
An HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on `8-index.html`)

Add more information to a Place `article`:
* List of Amenities:
  * tag `div`
  * classname `amenities`
  * margin top 40px
  * contains:
      * title:
          * tag `h2`
          * text `Amenities`
          * font size 16px
          * border bottom #DDDDDD 1px
      * list of amenities:
          * tag `ul` / `li`
          * no list style
          * icons on the left: [Pet friendly](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_pets.png), [TV](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_tv.png), [Wifi](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_wifi.png), etc… feel free to add more
* List of Reviews:
  * tag `div`
  * classname `reviews`
  * margin top 40px
  * contains:
      * title:
          * tag `h2`
          * text `Reviews`
          * font size 16px
          * border bottom #DDDDDD 1px
      * list of review:
          * tag `ul` / `li`
          * no list style
          * a review is described by:
              * `h3` tag for the user/date description (font size 14px). Ex: “From Bob Dylan the 27th January 2017”
              * `p` tag for the text (font size 12px)

Requirements:
* You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2` `h3`, `h4`, `ul`, `li` tags
* No inline style
* You are not allowed to use the `img` tag
* You are not allowed to use the `style` tag in the `head` tag
* All images must be stored in the `images` folder
* You must have 5 CSS files:
    * `styles/4-common.css`: for the global style (`body` and `.container` styles)
    * `styles/3-header.css`: for the header style
    * `styles/3-footer.css`: for the footer style
    * `styles/6-filters.css`: for the filters style
    * `styles/100-places.css`: for the places style

<img width="2160" alt="f54486a431a05ea3477e337e0e953686d3c6ffd0" src="https://github.com/elyse502/AirBnB_clone/assets/125453474/24ee9e61-b92c-43f7-82f2-9b1fea3e9d4f">

## 10. Flex: [101-index.html](101-index.html), [styles/4-common.css](styles/4-common.css), [styles/3-header.css](styles/3-header.css), [styles/3-footer.css](styles/3-footer.css), [styles/6-filters.css](styles/6-filters.css), [styles/101-places.css](styles/101-places.css), [images/](images/)
Improve the Places section by using [Flexible boxes](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) for all Place articles

[Flexbox Froggy](https://flexboxfroggy.com/)

## 11. Responsive design: [102-index.html](102-index.html), [styles/102-common.css](styles/102-common.css), [styles/102-header.css](styles/102-header.css), [styles/102-footer.css](styles/102-footer.css), [styles/102-filters.css](styles/102-filters.css), [styles/102-places.css](styles/102-places.css), [images/](images/)
mprove the page by adding [responsive design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design) to display correctly in mobile or small screens.

Examples:
* no horizontal scrolling
* redesign search bar depending of the width
* etc.

## 12. Accessibility: [103-index.html](103-index.html), [styles/103-common.css](styles/103-common.css), [styles/103-header.css](styles/103-header.css), [styles/103-footer.css](styles/103-footer.css), [styles/103-filters.css](styles/103-filters.css), [styles/103-places.css](styles/103-places.css), [images/](images/)
Improve the page by adding [Accessibility support](https://developer.mozilla.org/en-US/docs/Learn/Accessibility)

Examples:
* Colors contrast
* Header tags
* etc.















