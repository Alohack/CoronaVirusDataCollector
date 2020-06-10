

class Parser:
    # a static variable
    NumberOfCountries = 213
    # Number of parameters except countryName
    NumberOfParameters = 12

    def __init__(self, content):
        self.content = content

        # the class called mt_a occurs only once before countries
        # and it appears in the html code of each country, so we first pass the class declaration
        # and jump straight into the countries

        # finding the class mt_a declaration

        self.nextMTA = content.find("mt_a")
        self.currentCountryNumber = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.currentCountryNumber >= Parser.NumberOfCountries:
            raise StopIteration

        countryName, countryParameters = self.get_next_parameters()
        self.currentCountryNumber += 1

        return [countryName]+countryParameters

    def find_brackets_after(self, thisIndex):
        firstBracket = self.content.find('>', thisIndex)
        secondBracket = self.content.find('<', thisIndex)
        return firstBracket, secondBracket

    @staticmethod
    def remove_needless_symbols_from(thisString):
        return ''.join(x for x in thisString if x != ',' and x != '+' and x != ' ')

    def get_next_parameters(self):
        # finding the next country by finding the next mta
        self.nextMTA = self.content.find("mt_a", self.nextMTA + 1)
        firstBracket, secondBracket = self.find_brackets_after(self.nextMTA)

        # The country name is between firstBracket and secondBracket
        countryName = self.content[firstBracket + 1:secondBracket]
        countryParameters = []

        # the other parameters are in rows with "</td>"
        # and it occurs only once for each parameter
        nextTD = self.nextMTA
        for j in range(Parser.NumberOfParameters):
            nextTD = self.content.find("</td>", nextTD) + 10

            # We skip this line because it does not contain a parameter
            if j == 5:
                nextTD = self.content.find("</td>", nextTD) + 10

            firstBracket, secondBracket = self.find_brackets_after(nextTD)

            # This line has 2 signs of > and < so we skip the first of them
            if j == 11:
                firstBracket, secondBracket = self.find_brackets_after(secondBracket + 1)

            # The numeric parameters are between firstBracket and secondBracket
            # but the numbers are with commas and with + signs
            currentParameterWithCommas = self.content[firstBracket + 1:secondBracket]

            # removing the commas and + signs and putting only digits
            currentParameterWithoutCommas = Parser.remove_needless_symbols_from(currentParameterWithCommas)

            # in this website if the value is missing that means it contains 0
            if currentParameterWithoutCommas == "\n" or currentParameterWithoutCommas == "":
                currentParameterWithoutCommas = "0"
            countryParameters.append(currentParameterWithoutCommas)

        return countryName, countryParameters
