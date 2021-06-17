'''
A bunch of replacements on the scraped HTML.
'''

import re
from glob import glob

subs = [
    ('''        <li itemscope itemtype='http://schema.org/SiteNavigationElement'>
          <span itemprop='name'>
            <a href='https://iatistandard.org/en/privacy-policy/' itemprop="url">Privacy Policy </a>
          </span>
        </li>
''', ''),
    ('''    <!-- Global site tag (gtag.js) - Google Analytics -->
<script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-107364622-1"></script>
<script src="theme-javascripts/4253779dfdd8746a6d2d7a4caed66d6a3c739ecc.js_%3b%20filename_%3dUTF-8%27%274253779dfdd8746a6d2d7a4caed66d6a3c739ecc1522.js?__ws=discuss.iatistandard.org"></script>
''', ''),
    ('''		<div id="footer-cookie">
			<aside id="text-3" class="widget widget_text">
				<h3 class="widget-title">Cookie Disclaimer</h3>
				<div class="textwidget">
					<p>Cookies are small text files that are stored by the browser (e.g. Internet Explorer, Chrome, Firefox) on your computer or mobile phone. This site uses anonymous Analytics cookies which allow us to track how many unique individual users we have, and
						how often they visit the site. Unless a user signs in, these cookies cannot be used to identify an individual; they are used for statistical purposes only. If you are logged in, we will also know the details you gave to us for this, such as username
						and email address. By continuing to use this site, you are agreeing to the use of cookies.</p>
					<p><a href="https://www.aidtransparency.net/privacy-policy">Privacy policy</a></p>
				</div>
			</aside>
		</div>
''', ''),
    ('https://discuss.iatistandard.org', 'https://discuss.codeforiati.org'),
    (', best viewed with JavaScript enabled', ''),
    ('<li class="social twitter"><a href="https://twitter.com/IATI_aid">Twitter</a></li>', '<li class="social twitter"><a href="https://twitter.com/codeforiati">Twitter</a></li>'),
    ('''        <li itemscope itemtype='http://schema.org/SiteNavigationElement'>
          <span itemprop='name'>
            <a href='tos.html' itemprop="url">Terms of Service </a>
          </span>
        </li>
''', ''),
    ('''<div id="pre-footer">
	<div id="footer-additional">
		<div id="footer-social">
			<aside id="sidebar_social_links" class="widget widget_social_links">
				<div class="text-widget">
					<ul class="social-links">
						<li class="social twitter"><a href="https://twitter.com/codeforiati">Twitter</a></li>
						<li class="social rss"><a href="feed://support.iatistandard.org/home/index.rss">RSS</a></li>
					</ul>
				</div>
			</aside>
		</div>
		<!--#footer-social -->
	</div>
</div>
''', ''),
    ('''<nav>
    </nav>''', ''),
]
re_subs = [
    (r'''    <header>
      <a href="[^"]+">
          <img src="[^"]+" alt="IATI Community Discussions" id="site-logo" style="max-width: 150px;">
      </a>
    </header>
''', ''),
]

for file in glob('**/*.html', recursive=True):
    with open(file) as f:
        txt = f.read()
    for find, repl in subs:
        txt = txt.replace(find, repl)
    for find, repl in re_subs:
        txt = re.sub(find, repl, txt)
    with open(file, 'w') as f:
        _ = f.write(txt)
