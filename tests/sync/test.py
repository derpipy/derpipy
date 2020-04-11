import unittest
import iso8601
import datetime
from derpi.sync import client, Comment, Image, Intensities, Representations, DerpiModel, Tag, Post, User, Filter

null = None    # jSoN
false = False  # JsOn
true = True    # JsoN

DerpiModel._assert_consuming_all_params = False


class OnlineTest(unittest.TestCase):
    def test_comment(self):
        comment = client.comment(8927783)
        self.assertIsInstance(comment, Comment)
    # end def

    def test_image(self):
        image = client.image(1322277)
        self.assertIsInstance(image, Image)
    # end def

    def test_featured_image(self):
        featured_image = client.featured_image()
        self.assertIsInstance(featured_image, Image)
    # end def

    def test_tag(self):
        tag = client.tag('oc-colon-littlepip')
        self.assertIsInstance(tag, Tag)
    # end def

    def test_tag__aliased(self):
        tag = client.tag('littlepip')
        self.assertIsInstance(tag, Tag)
    # end def

    def test_post(self):
        post = client.post(4704912)
        self.assertIsInstance(post, Post)
    # end def

    def test_user(self):
        user = client.user(264159)
        self.assertIsInstance(user, User)
    # end def

    def test_filter(self):
        filter = client.filter(179331)
        self.assertIsInstance(filter, Filter)
    # end def
# end class


class OfflineTest(unittest.TestCase):
    def test_image(self):
        image = Image.from_dict({
        "image": {
            "mime_type": "image/png",
            "tag_ids": [24249, 26029, 27084, 28087, 29252, 33855, 36710, 38185, 40482, 41554, 41769, 42627, 43713, 44356, 45218, 47596, 48683, 49989, 54099, 60900, 70995, 75881, 82531, 83246, 98475, 109992, 129556, 140006, 141241, 169378, 173557, 178114, 186417, 187857, 191172, 210505, 234813, 243362, 355725, 373735, 377490, 407683],
            "comment_count": 63,
            "score": 1103,
            "downvotes": 11,
            "thumbnails_generated": true,
            "wilson_score": 0.9792839499360272,
            "source_url": "https://twitter.com/KamDrawings/status/1123822106784010240",
            "aspect_ratio": 1.7454090150250416,
            "sha512_hash": "ef377b5ce9b6abb39701bded38d9588e8ee6c28a6bc384d764237a9800356860484351be1f992c2c76a6db9425eb5171d260fde351c92e0615c4af7a3024156f",
            "orig_sha512_hash": "ef377b5ce9b6abb39701bded38d9588e8ee6c28a6bc384d764237a9800356860484351be1f992c2c76a6db9425eb5171d260fde351c92e0615c4af7a3024156f",
            "first_seen_at": "2019-05-02T05:33:36",
            "height": 1198,
            "intensities": {
              "ne": 43.666426229379056,
              "nw": 55.8670966658656,
              "se": 29.931677346829446,
              "sw": 43.073299224516546
            },
            "hidden_from_users": false,
            "name": "cacaw.png",
            "spoilered": false,
            "description": "bird.",
            "uploader": "Kam3E433",
            "tag_count": 42,
            "processed": true,
            "representations": {
              "full": "https://derpicdn.net/img/view/2019/5/2/2028858.png",
              "large": "https://derpicdn.net/img/2019/5/2/2028858/large.png",
              "medium": "https://derpicdn.net/img/2019/5/2/2028858/medium.png",
              "small": "https://derpicdn.net/img/2019/5/2/2028858/small.png",
              "tall": "https://derpicdn.net/img/2019/5/2/2028858/tall.png",
              "thumb": "https://derpicdn.net/img/2019/5/2/2028858/thumb.png",
              "thumb_small": "https://derpicdn.net/img/2019/5/2/2028858/thumb_small.png",
              "thumb_tiny": "https://derpicdn.net/img/2019/5/2/2028858/thumb_tiny.png"
            },
            "width": 2091,
            "id": 2028858,
            "deletion_reason": null,
            "view_url": "https://derpicdn.net/img/view/2019/5/2/2028858__safe_artist-colon-kam_gallus_sandbar_earth+pony_griffon_pony_airhorn_alarmed_behaving+like+a+bird_birb_birds+doing+bird+things_blue+background_blue+eye.png",
            "created_at": "2019-05-02T05:33:36",
            "updated_at": "2020-04-10T00:14:35",
            "faves": 813,
            "upvotes": 1114,
            "format": "png",
            "duplicate_of": null,
            "uploader_id": 459261,
            "tags": ["cute", "earth pony", "feather", "frown", "griffon", "male", "open mouth", "pony", "safe", "shocked", "simple background", "speech", "surprised", "text", "this will end in tears", "wings", "solo focus", "this will end in pain", "mismatched eyes", "caw", "airhorn", "alarmed", "featured image", "exclamation point", "wide eyes", "gradient background", "catbird", "behaving like a bird", "birb", "blue eyes", "blue background", "griffons doing bird things", "offscreen character", "spread wings", "hoof hold", "quadrupedal", "gallus", "this will end in deafness", "sandbar", "gallabetes", "birds doing bird things", "artist:kam"]
            },
            "interactions": []
        }['image'])
        expected = Image(aspect_ratio=1.7454090150250416, comment_count=63, created_at=datetime.datetime(2019, 5, 2, 5, 33, 36, tzinfo=datetime.timezone.utc), deletion_reason=None, description='bird.', downvotes=11, duplicate_of=None, faves=813, first_seen_at=datetime.datetime(2019, 5, 2, 5, 33, 36, tzinfo=datetime.timezone.utc), format='png', height=1198, hidden_from_users=False, id=2028858, intensities=Intensities(ne=43.666426229379056, nw=55.8670966658656, se=29.931677346829446, sw=43.073299224516546), mime_type='image/png', name='cacaw.png', orig_sha512_hash='ef377b5ce9b6abb39701bded38d9588e8ee6c28a6bc384d764237a9800356860484351be1f992c2c76a6db9425eb5171d260fde351c92e0615c4af7a3024156f', processed=True, representations=Representations(full='https://derpicdn.net/img/view/2019/5/2/2028858.png', large='https://derpicdn.net/img/2019/5/2/2028858/large.png', medium='https://derpicdn.net/img/2019/5/2/2028858/medium.png', small='https://derpicdn.net/img/2019/5/2/2028858/small.png', tall='https://derpicdn.net/img/2019/5/2/2028858/tall.png', thumb='https://derpicdn.net/img/2019/5/2/2028858/thumb.png', thumb_small='https://derpicdn.net/img/2019/5/2/2028858/thumb_small.png', thumb_tiny='https://derpicdn.net/img/2019/5/2/2028858/thumb_tiny.png'), score=1103, sha512_hash='ef377b5ce9b6abb39701bded38d9588e8ee6c28a6bc384d764237a9800356860484351be1f992c2c76a6db9425eb5171d260fde351c92e0615c4af7a3024156f', source_url='https://twitter.com/KamDrawings/status/1123822106784010240', spoilered=False, tag_count=42, tag_ids=[24249, 26029, 27084, 28087, 29252, 33855, 36710, 38185, 40482, 41554, 41769, 42627, 43713, 44356, 45218, 47596, 48683, 49989, 54099, 60900, 70995, 75881, 82531, 83246, 98475, 109992, 129556, 140006, 141241, 169378, 173557, 178114, 186417, 187857, 191172, 210505, 234813, 243362, 355725, 373735, 377490, 407683], tags=['cute', 'earth pony', 'feather', 'frown', 'griffon', 'male', 'open mouth', 'pony', 'safe', 'shocked', 'simple background', 'speech', 'surprised', 'text', 'this will end in tears', 'wings', 'solo focus', 'this will end in pain', 'mismatched eyes', 'caw', 'airhorn', 'alarmed', 'featured image', 'exclamation point', 'wide eyes', 'gradient background', 'catbird', 'behaving like a bird', 'birb', 'blue eyes', 'blue background', 'griffons doing bird things', 'offscreen character', 'spread wings', 'hoof hold', 'quadrupedal', 'gallus', 'this will end in deafness', 'sandbar', 'gallabetes', 'birds doing bird things', 'artist:kam'], thumbnails_generated=True, updated_at=datetime.datetime(2020, 4, 10, 0, 14, 35, tzinfo=datetime.timezone.utc), uploader='Kam3E433', uploader_id=459261, upvotes=1114, view_url='https://derpicdn.net/img/view/2019/5/2/2028858__safe_artist-colon-kam_gallus_sandbar_earth+pony_griffon_pony_airhorn_alarmed_behaving+like+a+bird_birb_birds+doing+bird+things_blue+background_blue+eye.png', width=2091, wilson_score=0.9792839499360272)
        self.assertEqual(image, expected)
    # end def

    def test_tag(self):
        tag = Tag.from_dict({
          "tag": {
            "aliased_tag": null,
            "aliases": [
              "littlepip"
            ],
            "category": "oc",
            "description": "Creator: Kkat\r\nSpecies: Unicorn Female\r\nMain protagonist of the \"Fallout: Equestria series\":http://www.fimfiction.net/story/119190/fallout-equestria  (NSFW)\r\n>>610341s",
            "dnp_entries": [],
            "id": 113046,
            "images": 3663,
            "implied_by_tags": [
              "futa+oc-colon-littlepip",
              "busty+littlepip",
              "pipabetes",
              "pipbutt"
            ],
            "implied_tags": [
              "fallout+equestria",
              "oc"
            ],
            "name": "oc:littlepip",
            "name_in_namespace": "littlepip",
            "namespace": "oc",
            "short_description": "",
            "slug": "oc-colon-littlepip",
            "spoiler_image_uri": null
          }
        }['tag'])
        expected = Tag(aliased_tag=None, aliases=['littlepip'], category='oc', description='Creator: Kkat\r\nSpecies: Unicorn Female\r\nMain protagonist of the "Fallout: Equestria series":http://www.fimfiction.net/story/119190/fallout-equestria  (NSFW)\r\n>>610341s', dnp_entries=[], id=113046, images=3663, implied_by_tags=['futa+oc-colon-littlepip', 'busty+littlepip', 'pipabetes', 'pipbutt'], implied_tags=['fallout+equestria', 'oc'], name='oc:littlepip', name_in_namespace='littlepip', namespace='oc', short_description='', slug='oc-colon-littlepip', spoiler_image=None, spoiler_image_uri=None)
        self.assertEqual(tag, expected)
    # end def

    def test_tag__aliased(self):
        tag = Tag.from_dict({
          "tag": {
            "aliased_tag": "oc-colon-littlepip",
            "aliases": [],
            "category": null,
            "description": "",
            "dnp_entries": [],
            "id": 33169,
            "images": 0,
            "implied_by_tags": [],
            "implied_tags": [],
            "name": "littlepip",
            "name_in_namespace": "littlepip",
            "namespace": null,
            "short_description": "",
            "slug": "littlepip",
            "spoiler_image_uri": null
          }
        }['tag'])
        expected = Tag(aliased_tag='oc-colon-littlepip', aliases=[], category=None, description='', dnp_entries=[], id=33169, images=0, implied_by_tags=[], implied_tags=[], name='littlepip', name_in_namespace='littlepip', namespace=None, short_description='', slug='littlepip', spoiler_image=None, spoiler_image_uri=None)
        self.assertEqual(tag, expected)

    def test_post(self):
        post = Post.from_dict({
          "post": {
            "author": "Joey",
            "avatar": "https://derpicdn.net/avatars/2019/11/13/14215782720827205181237247282992609700.png",
            "body": "This notice is primarily targeted towards developers, but may affect anyone using third party applications to update the site:\r\n\r\n*If you do not know what an API is and you only browse Derpibooru in a web browser, than this post does not affect you, and you can ignore this announcement.*\r\n\r\nIn December, Derpibooru completed the migration to \"Philomena\":https://github.com/derpibooru/philomena - our new, rewritten from the ground-up codebase - to significantly improve performance of the site and to pave the way for future enhancements.\r\n\r\nAs part of this migration, Philomena implements a new API that allows more capabilities than our previous API. You can read a bit about that \"here\":/forums/meta/topics/philomena-open-beta-breaking-api-changes\r\n\r\nThe old API has remained available since the migration to ensure compatibility with older apps and to allow third party developers time to migrate to the new API. Regrettably, maintaining compatibility with the old API is causing some limits with regards to changes we'd like to make to the site's code. As such, our development team has made the decision to begin deprecating and shutting down the old API.\r\n\r\nCurrently the old API is scheduled to be decommissioned on *March 31st, 2020*.\r\n\r\nIf you write third party apps or scripts that interact with Derpibooru, we encourage you to make sure that your application is compatible with the new API by then. You can read documentation on the current API \"here\":/pages/api\r\n\r\nIf you use an app or script that interacts with the site, and it has not been updated since December, then it is likely it's utilizing the old API still, and you should reach out to the developer to ensure that it's updated so compatibility is maintained.",
            "created_at": "2020-02-20T16:18:04",
            "edit_reason": null,
            "edited_at": "2020-02-21T05:42:40Z",
            "id": 4704912,
            "updated_at": "2020-02-21T05:42:40",
            "user_id": 216494
          }
        }['post'])
        expected = Post(author='Joey', body='This notice is primarily targeted towards developers, but may affect anyone using third party applications to update the site:\r\n\r\n*If you do not know what an API is and you only browse Derpibooru in a web browser, than this post does not affect you, and you can ignore this announcement.*\r\n\r\nIn December, Derpibooru completed the migration to "Philomena":https://github.com/derpibooru/philomena - our new, rewritten from the ground-up codebase - to significantly improve performance of the site and to pave the way for future enhancements.\r\n\r\nAs part of this migration, Philomena implements a new API that allows more capabilities than our previous API. You can read a bit about that "here":/forums/meta/topics/philomena-open-beta-breaking-api-changes\r\n\r\nThe old API has remained available since the migration to ensure compatibility with older apps and to allow third party developers time to migrate to the new API. Regrettably, maintaining compatibility with the old API is causing some limits with regards to changes we\'d like to make to the site\'s code. As such, our development team has made the decision to begin deprecating and shutting down the old API.\r\n\r\nCurrently the old API is scheduled to be decommissioned on *March 31st, 2020*.\r\n\r\nIf you write third party apps or scripts that interact with Derpibooru, we encourage you to make sure that your application is compatible with the new API by then. You can read documentation on the current API "here":/pages/api\r\n\r\nIf you use an app or script that interacts with the site, and it has not been updated since December, then it is likely it\'s utilizing the old API still, and you should reach out to the developer to ensure that it\'s updated so compatibility is maintained.', id=4704912, user_id=216494, avatar='https://derpicdn.net/avatars/2019/11/13/14215782720827205181237247282992609700.png', created_at=datetime.datetime(2020, 2, 20, 16, 18, 4, tzinfo=datetime.timezone.utc), edit_reason=None, edited_at=datetime.datetime(2020, 2, 21, 5, 42, 40, tzinfo=datetime.timezone.utc), updated_at=datetime.datetime(2020, 2, 21, 5, 42, 40, tzinfo=datetime.timezone.utc))
        self.assertEqual(post, expected)
    # end def

    def test_user(self):
        user = User.from_dict({
          "user": {
            "avatar_url": "https://derpicdn.net/avatars/2013/5/2/6960000e0c80e94df370222.png",
            "awards": [
              {
                "awarded_on": "2018-05-02T20:35:09Z",
                "id": 27,
                "image_url": "https://derpicdn.net/media/2016/8/23/540676fb2fd6546ee45a1c1.svg",
                "label": null,
                "title": "Artist"
              }
            ],
            "comments_count": 10,
            "created_at": "2013-05-02T16:07:03",
            "description": null,
            "id": 264159,
            "links": [
              {
                "created_at": "2018-05-02T20:42:44",
                "state": "verified",
                "tag_id": 53157,
                "user_id": 264159
              },
              {
                "created_at": "2018-05-02T20:33:00",
                "state": "verified",
                "tag_id": 53157,
                "user_id": 264159
              }
            ],
            "name": "luckydonald",
            "posts_count": 3,
            "role": "user",
            "slug": "luckydonald",
            "topics_count": 0,
            "uploads_count": 12
          }
        }['user'])
        expected = User(id=264159, name='luckydonald', slug='luckydonald', role='user', description=None, avatar_url='https://derpicdn.net/avatars/2013/5/2/6960000e0c80e94df370222.png', created_at=datetime.datetime(2013, 5, 2, 16, 7, 3, tzinfo=datetime.timezone.utc), comments_count=10, uploads_count=12, posts_count=3, topics_count=0, links=[{'created_at': '2018-05-02T20:42:44', 'state': 'verified', 'tag_id': 53157, 'user_id': 264159}, {'created_at': '2018-05-02T20:33:00', 'state': 'verified', 'tag_id': 53157, 'user_id': 264159}], awards=[{'awarded_on': '2018-05-02T20:35:09Z', 'id': 27, 'image_url': 'https://derpicdn.net/media/2016/8/23/540676fb2fd6546ee45a1c1.svg', 'label': None, 'title': 'Artist'}])
        self.assertEqual(user, expected)
    # emd def

    def test_filter(self):
        filter = Filter.from_dict({
          "filter": {
            "description": "Displays only images of Waifu horse.\r\n\r\nID: 179331",
            "hidden_complex": "score.lte:100\r\n-littlepip",
            "hidden_tag_ids": [115234, 26911],
            "id": 179331,
            "name": "Best Pony",
            "public": true,
            "spoilered_complex": null,
            "spoilered_tag_ids": [26707],
            "system": false,
            "user_count": 0,
            "user_id": 264159
          }
        }['filter'])
        expected = Filter(id=179331, name='Best Pony', description='Displays only images of Waifu horse.\r\n\r\nID: 179331', user_id=264159, user_count=0, system=False, public=True, spoilered_tag_ids=[26707], spoilered_complex=None, hidden_tag_ids=[115234, 26911], hidden_complex='score.lte:100\r\n-littlepip')
        self.assertEqual(filter, expected)
    # emd def

    def est_cls(self):
        cls = Cls.from_dict({}['cls'])
        expected = Cls()
        self.assertEqual(cls, expected)
    # emd def

if __name__ == '__main__':
    unittest.main()
