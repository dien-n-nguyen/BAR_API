import re
import redis
import os


class BARUtils:
    @staticmethod
    def error_exit(msg):
        """Exit if failed
        :param msg: message to pass on failure
        :return:
        """
        result = {"wasSuccessful": False, "error": msg}
        return result

    @staticmethod
    def success_exit(msg):
        """Output if success
        :param msg: the actual data the needs to be output
        :return:
        """
        result = {"wasSuccessful": True, "data": msg}
        return result

    @staticmethod
    def is_arabidopsis_gene_valid(gene):
        """This function verifies if Arabidopsis gene is valid
        :param gene:
        :return:
        """
        if re.search(r"^At[12345cm]g\d{5}.?\d?$", gene, re.I):
            return True
        else:
            return False

    @staticmethod
    def is_poplar_gene_valid(gene):
        """This function verifies if Poplar v3 gene is valid
        :param gene:
        :return: True if valid
        """
        if re.search(r"^POTRI\.\d{3}g\d{6}.?\d{0,3}$", gene, re.I):
            return True
        else:
            return False

    @staticmethod
    def is_rice_gene_valid(gene, isoform_id=False):
        """This function verifies if rice gene is valid
        :param gene:
        :param isoform_id: True if you want to verifiy isoform ID
        :return: True if valid
        """
        if isoform_id and re.search(r"^LOC_Os\d{2}g\d{5}\.\d{1,2}$", gene, re.I):
            return True
        elif isoform_id is False and re.search(r"^LOC_Os\d{2}g\d{5}$", gene, re.I):
            return True
        else:
            return False

    @staticmethod
    def is_tomato_gene_valid(gene, isoform_id=False):
        """This function verifies if ITAG Solyc gene is valid
        :param gene:
        :param isoform_id: True if you want to verifiy isoform ID
        :return: True if valid
        """
        if isoform_id and re.search(r"^Solyc\d\dg\d{6}\.\d\.\d$", gene, re.I):
            return True
        elif isoform_id is False and re.search(r"^Solyc\d\dg\d{6}$", gene, re.I):
            return True
        else:
            return False

    @staticmethod
    def is_cannabis_gene_valid(gene):
        """This function verifies if cannabis gene is valid: AGQN03000001
        :param gene:
        :return: True if valid
        """
        if gene and re.search(r"^AGQN\d{0,10}$", gene, re.I):
            return True
        else:
            return False

    @staticmethod
    def is_integer(data):
        """Check if the input is at max ten figure number.
        :param data: int number
        :return: True if a number
        """
        if re.search(r"^\d{1,10}$", data):
            return True
        else:
            return False

    @staticmethod
    def format_poplar(poplar_gene):
        """Format Poplar gene ID to be Potri.016G107900, i.e. capitalized P and G
        :param poplar_gene: gene id
        :return: String
        """
        return poplar_gene.translate(str.maketrans("pOTRIg", "PotriG"))

    @staticmethod
    def connect_redis():
        """This function connects to redis
        :returns: redis connection
        """
        r = redis.Redis(
            host="localhost", port=6379, password=os.environ.get("BAR_REDIS_PASSWORD")
        )

        return r
