import os
import pandas as pd
from strsimpy.levenshtein import Levenshtein
from strsimpy.normalized_levenshtein import NormalizedLevenshtein
from valentine import valentine_match, valentine_metrics
from valentine.algorithms import Coma, Cupid, DistributionBased, JaccardLevenMatcher, SimilarityFlooding


class SchemaMatchingSystem():
    def __init__(self):
        self.levenshtein = Levenshtein()
        self.mapping_columns = {
            "City": ["City", "Thành phố", "Tên thành phố"],
            "Hotel name": ["Hotel name", "Tên Khách sạn"],
            "Image": ["Image", "image", "Ảnh", "Ảnh minh họa"],
            "Url": ["Url", "short-link", "Link", "short_url"],
            "Address": ["Address", "Địa chỉ"],
            "Stars": ["Stars", "Số sao"],
            "Min Price": ["Giá", "Giá thấp nhất", "Min Price", "Price"],
            "Rating": ["Rating", "Đánh giá"],
            "Number of reviews": ["Number of reviews", "num_reviews"],
            "Reviews": ["Reviews"],
            "Facilities": ["Facilities", "CSVC", "Cơ sở vật chất"],
            "Description": ["Description", "Mô tả"],
            "Nearby places": ["Nearby places", "Địa điểm xung quanh"]
        }

    def getTargetSchema(self):
        target_schema = []
        for col in self.mapping_columns:
            target_schema.append(col)
        return target_schema

    def similarity_score(self, x, y):
        x = x.lower().strip()
        y = y.lower().strip()
        return (len(x) + len(y) - self.levenshtein.distance(x, y)) / (len(x) + len(y))

    def check_similarity(self, x, y, threshold=0.8):

        score = self.similarity_score(x, y)
        if score > threshold:
            return True
        return False

    def schema_matching(self, cols, threshold=0.85):

        res = dict()
        for colum in cols:
            for key in self.mapping_columns:
                listMatching = self.mapping_columns[key]
                for match in listMatching:
                    score = self.similarity_score(colum, match)
                    if(score > threshold):
                        print("{0:20}\t{0:20}\t".format(
                            colum, match) + str(score))
                        res[colum] = key
        return res

    def matchedCol(result):
        matched_col = []
        source_col = []
        for key in result:
            matched_col.append(result[key])
            source_col.append(key)

        return (matched_col, source_col)
