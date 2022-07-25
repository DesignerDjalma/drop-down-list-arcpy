import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        param0 = arcpy.Parameter(
            displayName ='Input Features',
            name ='in_features',
            datatype ="GPString",
            parameterType ='Required',
            direction ='Input')

        param1 = arcpy.Parameter(
            displayName='Statistics Field(s)',
            name='stat_fields',
            datatype= 'GPString',
            parameterType='Required',
            direction='Input')
        # param1.parameterDependencies = [param0.name]
        # param1.columns = [['Field', 'Field'], ['GPString', 'Statistic Type']]
        # param1.filters[1].type = 'ValueList'
        # param1.values = [['NAME', 'SUM']]
        # param1.filters[1].list = ['SUM', 'MIN', 'MAX', 'STDEV', 'MEAN']

        param0.filter.list = ['REGULARIZAÇÃO NÃO ONEROSA','REGULARIZAÇÃO ONEROSA', 'OUTRO']
        params = [param0, param1]


        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""


        if parameters[0].altered:
            parameters[1].value = parameters[1].valueAsText
            #parameters[1].value = "aaaaaaaaaaa"



        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return
