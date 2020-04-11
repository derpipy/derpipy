import unittest
import iso8601
import datetime
from derpi.sync import client, Comment, Image, Intensities, Representations, DerpiModel

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
        expected = Image(aspect_ratio=1.7454090150250416, comment_count=63, created_at=datetime.datetime(2019, 5, 2, 5, 33, 36, tzinfo=datetime.timezone.utc), deletion_reason=None, description='bird.', downvotes=11, duplicate_of=None, faves=813, first_seen_at=datetime.datetime(2019, 5, 2, 5, 33, 36, tzinfo=datetime.timezone.utc), format='png', height=1198, hidden_from_users=False, id=2028858, intensities=None, mime_type='image/png', name='cacaw.png', orig_sha512_hash='ef377b5ce9b6abb39701bded38d9588e8ee6c28a6bc384d764237a9800356860484351be1f992c2c76a6db9425eb5171d260fde351c92e0615c4af7a3024156f', processed=True, representations=Representations(full='https://derpicdn.net/img/view/2019/5/2/2028858.png', large='https://derpicdn.net/img/2019/5/2/2028858/large.png', medium='https://derpicdn.net/img/2019/5/2/2028858/medium.png', small='https://derpicdn.net/img/2019/5/2/2028858/small.png', tall='https://derpicdn.net/img/2019/5/2/2028858/tall.png', thumb='https://derpicdn.net/img/2019/5/2/2028858/thumb.png', thumb_small='https://derpicdn.net/img/2019/5/2/2028858/thumb_small.png', thumb_tiny='https://derpicdn.net/img/2019/5/2/2028858/thumb_tiny.png'), score=1103, sha512_hash='ef377b5ce9b6abb39701bded38d9588e8ee6c28a6bc384d764237a9800356860484351be1f992c2c76a6db9425eb5171d260fde351c92e0615c4af7a3024156f', source_url='https://twitter.com/KamDrawings/status/1123822106784010240', spoilered=False, tag_count=42, tag_ids=[24249, 26029, 27084, 28087, 29252, 33855, 36710, 38185, 40482, 41554, 41769, 42627, 43713, 44356, 45218, 47596, 48683, 49989, 54099, 60900, 70995, 75881, 82531, 83246, 98475, 109992, 129556, 140006, 141241, 169378, 173557, 178114, 186417, 187857, 191172, 210505, 234813, 243362, 355725, 373735, 377490, 407683], tags=['cute', 'earth pony', 'feather', 'frown', 'griffon', 'male', 'open mouth', 'pony', 'safe', 'shocked', 'simple background', 'speech', 'surprised', 'text', 'this will end in tears', 'wings', 'solo focus', 'this will end in pain', 'mismatched eyes', 'caw', 'airhorn', 'alarmed', 'featured image', 'exclamation point', 'wide eyes', 'gradient background', 'catbird', 'behaving like a bird', 'birb', 'blue eyes', 'blue background', 'griffons doing bird things', 'offscreen character', 'spread wings', 'hoof hold', 'quadrupedal', 'gallus', 'this will end in deafness', 'sandbar', 'gallabetes', 'birds doing bird things', 'artist:kam'], thumbnails_generated=True, updated_at=datetime.datetime(2020, 4, 10, 0, 14, 35, tzinfo=datetime.timezone.utc), uploader='Kam3E433', uploader_id=459261, upvotes=1114, view_url='https://derpicdn.net/img/view/2019/5/2/2028858__safe_artist-colon-kam_gallus_sandbar_earth+pony_griffon_pony_airhorn_alarmed_behaving+like+a+bird_birb_birds+doing+bird+things_blue+background_blue+eye.png', width=2091, wilson_score=0.9792839499360272)
        self.assertEqual(image, expected)
    # end def


if __name__ == '__main__':
    unittest.main()
