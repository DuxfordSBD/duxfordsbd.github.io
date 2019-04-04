---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
header:
  image_fullwidth: duxford-soapbox-derby-header.jpg
widget1:
  title: "About the Derby"
  url: '/about/'
  image: widget-1.jpg
  text: "The Duxford Soapbox Derby was established in 2013 to raise money for Cancer Research UK in memory of Phil Hill. It's a  wonderful chaotic dash around the village by would be grand prix stars racing in anything from a wheelbarrow to an old iron bath."
widget2:
  title: "Taking part"
  url: '/participating/rules'
  image: widget-2.jpg
  text: 'Entries to the cart race are limited and will be allocated on a first come, first served basis. Applications must be received by 31st August 2019.'
widget3:
  title: "Photo and Video Gallery"
  url: '/gallery/2018-photos'
  text: 'We have lots of photos and videos from our previous events. Take a look and see if you can get some inspiration for your own cart design!'
  video: '<a href="#" data-reveal-id="videoModal"><img src="https://duxfordsbd.github.io/SBD_web/images/widget-3.png"" width="302" height="200" alt=""/></a>'
#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
callforaction:
  url: https://fundraise.cancerresearchuk.org/unite/duxford-soap-box-derby-2019?_ga=2.103161541.437085530.1552899240-1415119213.1551092232
  text: Donate to our CRUK fundraising page  ›
  style: alert
permalink: /index.html
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
---
<div id="videoModal" class="reveal-modal large" data-reveal="">
  <div class="flex-video widescreen vimeo" style="display: block;">
    <iframe width="640" height="360" src="https://www.youtube.com/embed/Z8McY2qDswI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>
  <a class="close-reveal-modal">&#215;</a>
</div>
