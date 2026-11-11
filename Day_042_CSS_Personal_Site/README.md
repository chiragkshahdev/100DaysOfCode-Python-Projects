# Day 42 - CSS Personal Site

Upgraded version of Day 41 Personal Site. Now styled with External CSS, Google Fonts and proper layout.

## Demo
Open `index.html` in any browser. No server needed.

## Files
- `index.html` - Main Personal Site
- `contact.html` - Contact Page
- `styles.css` - All Styling (External CSS)

## Features
- Top Container with Cloud and Mountain layout
- Profile Section with Intro
- My Skills Section with Float Images
- Get In Touch Section with Gradient Button
- Bottom Footer with Social Links (LinkedIn, GitHub, Instagram)
- Contact Page

## Sections Explained
1. **Top Container:** Name, "a programmer" title, clouds, mountain image
2. **Profile:** Round profile photo, Hello, Intro text
3. **Skills:** Python Development (image left), Web Development (image right)
4. **Contact Me:** Message + CONTACT ME button
5. **Footer:** Teal background, social links, copyright

## Tech Used
- HTML
- CSS (External)
- Google Fonts: Sacramento, Montserrat, Merriweather
- CSS Concepts: Position, Float, Margin, Padding, Gradient, Hover

## CSS Concepts Learned
- `position: relative` and `position: absolute` for clouds
- `float: left` / `float: right` for skill images
- `text-align: center` for full page
- `border-radius: 50%` for round profile photo
- `linear-gradient` for button
- `:hover` effect for links and button
- `width: 30% / 50%` for centered content

## How to Customize
1. Change Your Name in `index.html` - `<h1>I'm Your Name.</h1>`
2. Change Profile Photo - Replace `src` in profile image
3. Change Skills Text - Edit inside `.skill-row`
4. Change Social Links - Edit `href` in `.bottom-container`
5. Change Colors - Edit in `styles.css` - `#66BFBF`, `#11999E`, `#E4F9F5`

## Colors Used
- Background Top: `#E4F9F5`
- Headings: `#66BFBF`
- Sub Headings: `#11999E`
- Text: `#40514E`
- Footer: `#66BFBF`
- Button: `#11cdd4` to `#11999e`

## How to Run
1. Keep all 3 files in same folder
2. Double-click `index.html`
3. It will open in browser

## Day 41 vs Day 42
- Day 41: Basic HTML, Internal CSS, Table layout
- Day 42: External CSS, Div layout, Fonts, Position, Float, Beautiful Design