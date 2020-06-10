from object import Item


class Parser:

    def __init__(self):
        Parser.NumberOfCountries = 213

    def parse_object(self, content):
        countryName, countryParameters = self.get_other_parameters(content)
        return Item(
            property_1=countryName,
            property_2=countryParameters[0],
            property_3=countryParameters[1],
            property_4=countryParameters[2],
            property_5=countryParameters[3],
            property_6=countryParameters[4],
            property_7=countryParameters[5],
            property_8=countryParameters[6],
            property_9=countryParameters[7],
            property_10=countryParameters[8],
            property_11=countryParameters[9],
            property_12=countryParameters[10],
            property_13=countryParameters[11],
        )

    @staticmethod
    def find_brackets_after(thisIndex, content):
        firstBracket = content.find('>', thisIndex)
        secondBracket = content.find('<', thisIndex)
        return firstBracket, secondBracket

    @staticmethod
    def remove_needless_symbols_from(thisString):
        return ''.join(x for x in thisString if x != ',' and x != '+' and x != ' ')

    def get_other_parameters(self, content):

        countryName = []
        countryParameters = [[] for i in range(12)]

        # the class called mt_a occurs only once before countries
        # and it appears in the html code of each country, so we first pass the class declaration
        # and jump straight into the countries

        # finding the class mt_a declaration
        nextMTA = content.find("mt_a")

        for i in range(0, Parser.NumberOfCountries):
            # finding the next country by finding the next mta
            nextMTA = content.find("mt_a", nextMTA + 1)
            firstBracket, secondBracket = Parser.find_brackets_after(nextMTA, content)

            # The country name is between firstBracket and secondBracket
            currentName = content[firstBracket + 1:secondBracket]
            countryName.append(currentName)

            # the other parameters are in rows with "</td>"
            # and it occurs only once for each parameter
            nextTD = nextMTA
            for j in range(12):
                nextTD = content.find("</td>", nextTD) + 10

                # We skip this line because it does not contain a parameter
                if j == 5:
                    nextTD = content.find("</td>", nextTD) + 10

                firstBracket, secondBracket = Parser.find_brackets_after(nextTD, content)

                # This line has 2 signs of > and < so we skip the first of them
                if j == 11:
                    firstBracket, secondBracket = Parser.find_brackets_after(secondBracket + 1, content)

                # The numeric parameters are between firstBracket and secondBracket
                # but the numbers are with commas and with + signs
                currentParameterWithCommas = content[firstBracket + 1:secondBracket]

                # removing the commas and + signs and putting only digits
                currentParameterWithoutCommas = Parser.remove_needless_symbols_from(currentParameterWithCommas)

                # in this website if the value is missing that means it contains 0
                if currentParameterWithoutCommas == "\n" or currentParameterWithoutCommas == "":
                    currentParameterWithoutCommas = "0"
                countryParameters[j].append(currentParameterWithoutCommas)

        return countryName, countryParameters
