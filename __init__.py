"""
MastadonSocialSkill Search Mycroft Skill.
"""

import sys
import re
import operator
import base64
from os.path import dirname
from traceback import print_exc
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'aix'

LOGGER = getLogger(__name__)


class MastadonSocialSkill(MycroftSkill):
    """
    MastadonSocialSkill Skill Class.
    """

    def __init__(self):
        """
        MastadonSocialSkill Skill Class.
        """
        super(MastadonSocialSkill, self).__init__(
            name="MastadonSocialSkill")

    @intent_handler(IntentBuilder("MastadonTootKeywordIntent").require("MastadonTootKeyword").build())
    def handle_mastadon_social_skill_intent(self, message):
        """
        Mastadon Toot
        """
        mastodon = self.authorize()
        utterance = message.data.get('utterance').lower()
        utterance = utterance.replace(message.data.get('MastadonTootKeyword'), '')
        searchString = utterance
        mastodon.toot(utterance)

    @intent_handler(IntentBuilder("MastadonGetLastKeywordIntent").require("MastadonGetLastKeyword").build())
    def handle_mastadon_social_skill_intent(self, message):
        """
        Mastadon Toot
        """
        mastodon = self.authorize()
        masFetch = mastodon.timeline(timeline='home', max_id=None, since_id=None, limit=None)
        contentText = masFetch[0]['content']
        speakText = self.fixSpeak(contentText)
        self.speak(speakText)

    def authorize(self):
        """
        Your Login Details Here
        """
        mastodon = Mastodon(
            client_id="",
            client_secret="",
            access_token="",
            api_base_url="https://mastodon.social"
        )
        return mastodon        
    
    def fixSpeak(content):
        fixRemove = re.compile('<.*?>')
        fixtext = re.sub(fixRemove, '', content)
        return fixtext
    
    def stop(self):
        """
        Mycroft Stop Function
        """
        pass


def create_skill():
    """
    Mycroft Create Skill Function
    """
    return MastadonSocialSkill()
