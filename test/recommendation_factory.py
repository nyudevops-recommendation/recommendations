# Copyright 2016, 2019 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice
from service.models import Recommendation


class RecommendationFactory(factory.Factory):
    """ Creates fake recommendations that you don't have to feed """

    class Meta:
        model = Recommendation

    id = factory.Sequence(lambda n: n)
    product_id = factory.Sequence(lambda n: n + 1)
    customer_id = factory.Sequence(lambda n: n + 2)
    recommend_type = FuzzyChoice(choices=["upsell", "crosssell", "accessory", "downsell"])
    recommend_product_id = factory.Sequence(lambda n: n + 3)
    rec_success = 0


if __name__ == '__main__':
    for _ in range(10):
        recommendation = RecommendationFactory()
        print(recommendation.serialize())
