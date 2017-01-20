#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
    fortunes = [
    "I see much code in your future.",
    "Consider eating more cookies.",
    "You've tamed the Python, now free it upon the spider's web."
    ]

    return random.choice(fortunes)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortuneParagraph = "<p>Your fortune is: " + fortune + "</p>"

        header = "<h1>Fortune Cookies</h1>"

        luckyNumber = "<strong>" + str(random.randint(1, 100)) + "</strong>"
        luckySentence ='<p>Your lucky number is: ' + luckyNumber +"</p>"

        cookieAgain = '<a href="."><button>Another Cookie Please</button></a>'

        content = header + fortuneParagraph + luckySentence + cookieAgain
        self.response.write(content)


routes = [
    ('/', MainHandler)
]

app = webapp2.WSGIApplication(routes, debug = True)
