meta/relational/mapping


class ColumnMapping(Any):

    def __init__(self, columnName:str, relationalOperationElement:RelationalOperationElement):
        self.columnName = columnName
        self.relationalOperationElement = relationalOperationElement


class RelationalInstanceSetImplementation(InstanceSetImplementation):

    def __init__(self, primaryKey:list[RelationalOperationElement]=[]):
        self.primaryKey = primaryKey


class FilterMapping(Any):

    def __init__(self, database:Database, filterName:str, filter:Filter, setMappingOwner:RelationalInstanceSetImplementation=None, joinTreeNode:JoinTreeNode=None):
        self.database = database
        self.filterName = filterName
        self.filter = filter
        self.setMappingOwner = setMappingOwner
        self.joinTreeNode = joinTreeNode


class GroupByMapping(Any):

    def __init__(self, setMappingOwner:RelationalInstanceSetImplementation=None, columns:list[RelationalOperationElement]=[]):
        self.setMappingOwner = setMappingOwner
        self.columns = columns


class RootRelationalInstanceSetImplementation(RelationalInstanceSetImplementation,RelationalMappingSpecification):

    def __init__(self):


class EmbeddedRelationalInstanceSetImplementation(EmbeddedSetImplementation,RelationalInstanceSetImplementation):

    def __init__(self, setMappingOwner:RootRelationalInstanceSetImplementation):
        self.setMappingOwner = setMappingOwner


class OtherwiseEmbeddedRelationalInstanceSetImplementation(EmbeddedRelationalInstanceSetImplementation,OtherwiseEmbeddedSetImplementation):

    def __init__(self):


class InlineEmbeddedRelationalInstanceSetImplementation(EmbeddedRelationalInstanceSetImplementation,InlineEmbeddedSetImplementation):

    def __init__(self):


class RelationalPropertyMapping(PropertyMapping):

    def __init__(self, relationalOperationElement:RelationalOperationElement, transformer:ValueTransformer=None):
        self.relationalOperationElement = relationalOperationElement
        self.transformer = transformer


class RelationalAssociationImplementation(AssociationImplementation):

    def __init__(self):


class SemiStructuredRelationalPropertyMapping(RelationalPropertyMapping):

    def __init__(self):


class SemiStructuredEmbeddedRelationalInstanceSetImplementation(SemiStructuredRelationalPropertyMapping,EmbeddedRelationalInstanceSetImplementation):

    def __init__(self):


class SemiStructuredRelationalInstanceSetImplementation(RootRelationalInstanceSetImplementation):

    def __init__(self):


class RelationalActivity(Activity):

    def __init__(self, sql:str, comment:str=None, executionTimeInNanoSecond:int=None, sqlGenerationTimeInNanoSecond:int=None, connectionAcquisitionTimeInNanoSecond:int=None, executionPlanInformation:str=None, dataSource:DataSource=None):
        self.sql = sql
        self.comment = comment
        self.executionTimeInNanoSecond = executionTimeInNanoSecond
        self.sqlGenerationTimeInNanoSecond = sqlGenerationTimeInNanoSecond
        self.connectionAcquisitionTimeInNanoSecond = connectionAcquisitionTimeInNanoSecond
        self.executionPlanInformation = executionPlanInformation
        self.dataSource = dataSource


class TableTDS(TabularDataSetImplementation):

    def __init__(self, table:NamedRelation):
        self.table = table


class BuilderInfo(Any):

    def __init__(self, class:Class, milestoningStrategy:Function, sqlNull:SQLNull, static:StaticMappingInstanceData, keys:list[str]=[], transforms:list[Function]=[], indices:list[int]=[], pks:list[int]=[], propLookUpIndices:list[int]=[]):
        self.class = class
        self.milestoningStrategy = milestoningStrategy
        self.sqlNull = sqlNull
        self.static = static
        self.keys = keys
        self.transforms = transforms
        self.indices = indices
        self.pks = pks
        self.propLookUpIndices = propLookUpIndices


class KeyInformation(MappingInstanceData):

    def __init__(self, sourceConnection:Connection, buildMethod:BuildMethod, pk:list[Any]=[]):
        self.sourceConnection = sourceConnection
        self.buildMethod = buildMethod
        self.pk = pk


class BuildMethod(Enum):
    TypeQuery = auto()

class SQLResultColumn(Any):

    def __init__(self, label:str, dataType:DataType=None):
        self.label = label
        self.dataType = dataType


class TempTableColumnMetaData(Any):

    def __init__(self, column:SQLResultColumn, identifierForGetter:str=None, parametersForGetter:Map=None):
        self.column = column
        self.identifierForGetter = identifierForGetter
        self.parametersForGetter = parametersForGetter


class QueryMetadata(Any):

    def __init__(self):


class TableInfo(QueryMetadata):

    def __init__(self, info:list[TableIdentifier]=[]):
        self.info = info


class TableIdentifier(Any):

    def __init__(self, schema:str, table:str):
        self.schema = schema
        self.table = table


class SQLExecutionNode(ExecutionNode):

    def __init__(self, sqlQuery:str, connection:DatabaseConnection, sqlComment:str=None, onConnectionCloseCommitQuery:str=None, onConnectionCloseRollbackQuery:str=None, resultColumns:list[SQLResultColumn]=[], metadata:list[QueryMetadata]=[], isResultColumnsDynamic:bool=None):
        self.sqlQuery = sqlQuery
        self.connection = connection
        self.sqlComment = sqlComment
        self.onConnectionCloseCommitQuery = onConnectionCloseCommitQuery
        self.onConnectionCloseRollbackQuery = onConnectionCloseRollbackQuery
        self.resultColumns = resultColumns
        self.metadata = metadata
        self.isResultColumnsDynamic = isResultColumnsDynamic


class RelationalSaveNode(ExecutionNode):

    def __init__(self, sqlQuery:str, connection:DatabaseConnection, generatedVariableName:str, columnValueGenerators:Map, sqlComment:str=None, onConnectionCloseCommitQuery:str=None, onConnectionCloseRollbackQuery:str=None):
        self.sqlQuery = sqlQuery
        self.connection = connection
        self.generatedVariableName = generatedVariableName
        self.columnValueGenerators = columnValueGenerators
        self.sqlComment = sqlComment
        self.onConnectionCloseCommitQuery = onConnectionCloseCommitQuery
        self.onConnectionCloseRollbackQuery = onConnectionCloseRollbackQuery


class RelationalInstantiationExecutionNode(ExecutionNode):

    def __init__(self):


class RelationalTdsInstantiationExecutionNode(RelationalInstantiationExecutionNode):

    def __init__(self):


class RelationalClassInstantiationExecutionNode(RelationalInstantiationExecutionNode):

    def __init__(self):


class RelationalRelationDataInstantiationExecutionNode(RelationalInstantiationExecutionNode):

    def __init__(self):


class RelationalDataTypeInstantiationExecutionNode(RelationalInstantiationExecutionNode):

    def __init__(self):


class CreateAndPopulateTempTableExecutionNode(ExecutionNode):

    def __init__(self, tempTableName:str, connection:DatabaseConnection, inputVarNames:list[str]=[], tempTableColumnMetaData:list[TempTableColumnMetaData]=[]):
        self.tempTableName = tempTableName
        self.connection = connection
        self.inputVarNames = inputVarNames
        self.tempTableColumnMetaData = tempTableColumnMetaData


class PostProcessorResult(Any):

    def __init__(self, query:SQLQuery, resultPostProcessor:list[Function]=[], executionNodes:list[ExecutionNode]=[], postExecutionNodes:list[ExecutionNode]=[], finallyExecutionNodes:list[ExecutionNode]=[], templateFunctions:list[str]=[]):
        self.query = query
        self.resultPostProcessor = resultPostProcessor
        self.executionNodes = executionNodes
        self.postExecutionNodes = postExecutionNodes
        self.finallyExecutionNodes = finallyExecutionNodes
        self.templateFunctions = templateFunctions


class PreAndFinallyExecutionSQLQuery(Any):

    def __init__(self, preQueryExecutionSQLQuery:str=None, finallyQueryExecutionSQLQuery:str=None):
        self.preQueryExecutionSQLQuery = preQueryExecutionSQLQuery
        self.finallyQueryExecutionSQLQuery = finallyQueryExecutionSQLQuery
