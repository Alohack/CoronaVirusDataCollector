from bs4 import BeautifulSoup


class Parser:
    # a static variable
    NUMBER_OF_COUNTRIES = 213
    # Number of parameters except countryName
    NUMBER_OF_PARAMETERS = 13

    def __init__(self, content):
        # all countries are mt_a class objects
        soup = BeautifulSoup(content, features="html.parser")
        self.mt_aObjects = soup.findAll("a", {"class": "mt_a"})
        self.currentCountryIndex = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.currentCountryIndex >= Parser.NUMBER_OF_COUNTRIES:
            self.currentCountryIndex = 0
            raise StopIteration

        countryParameters = self.get_next_parameters()
        self.currentCountryIndex += 1

        return countryParameters

    @staticmethod
    def remove_needless_symbols_from(thisString):
        return ''.join(x for x in thisString if x != ',' and x != '+' and x != ' ')

    def get_next_parameters(self):
        currentTag = self.mt_aObjects[self.currentCountryIndex]

        # the country name is our first parameter
        countryParameters = [currentTag.string]

        # the other parameters are in rows with tag "td"
        # the first td is the parent tag to the current tag
        currentTag = currentTag.parent
        for j in range(Parser.NUMBER_OF_PARAMETERS):
            # finding the next "td" sibling to our tag
            currentTag = currentTag.find_next_sibling("td")

            # We skip this line because it does not contain a parameter
            if j == 5:
                currentTag = currentTag.find_next_sibling("td")

            # The text can contain symbols like commas
            currentParameterWithCommas = str(currentTag.text)

            # removing the commas and + signs (There is no such thing with 12th one which is the mainland)
            if j < 12:
                currentParameterWithoutCommas = Parser.remove_needless_symbols_from(currentParameterWithCommas)
            else:
                currentParameterWithoutCommas = currentParameterWithCommas

            # in this website if the value is missing that means it contains 0
            if currentParameterWithoutCommas == "\n" or currentParameterWithoutCommas == "":
                currentParameterWithoutCommas = "0"
            countryParameters.append(currentParameterWithoutCommas)

        return countryParameters
