meta/relational/metamodel


class Database(SetBasedStore):

    def __init__(self, schemas:list[Schema]=[], joins:list[Join]=[], filters:list[Filter]=[]):
        self.schemas = schemas
        self.joins = joins
        self.filters = filters


class Schema(Namespace):

    def __init__(self, name:str, database:Database, tables:list[Table]=[], views:list[View]=[], tabularFunctions:list[TabularFunction]=[]):
        self.name = name
        self.database = database
        self.tables = tables
        self.views = views
        self.tabularFunctions = tabularFunctions


class RelationalMappingSpecification(Any):

    def __init__(self, userDefinedPrimaryKey:bool, mainTableAlias:TableAlias, filter:FilterMapping=None, distinct:bool=None, groupBy:GroupByMapping=None):
        self.userDefinedPrimaryKey = userDefinedPrimaryKey
        self.mainTableAlias = mainTableAlias
        self.filter = filter
        self.distinct = distinct
        self.groupBy = groupBy


class Filter(Any):

    def __init__(self, name:str, operation:Operation, database:Database=None):
        self.name = name
        self.operation = operation
        self.database = database


class Alias(RelationalOperationElement):

    def __init__(self, name:str, relationalElement:RelationalOperationElement):
        self.name = name
        self.relationalElement = relationalElement


class SQLQuery(RelationalOperationElement):

    def __init__(self, comment:str=None):
        self.comment = comment


class TableAlias(Alias):

    def __init__(self, relation:Relation, setMappingOwner:PropertyMappingsImplementation=None, database:Database=None, schema:str=None):
        self.relation = relation
        self.setMappingOwner = setMappingOwner
        self.database = database
        self.schema = schema


class Column(RelationalOperationElement,SetColumn):

    def __init__(self, name:str, type:DataType, nullable:bool=None, owner:Relation=None):
        self.name = name
        self.type = type
        self.nullable = nullable
        self.owner = owner


class RelationalOperationElement(Any):

    def __init__(self):


class MultiGrainFilter(Filter):
    """Indicates that the filter is a filter on the grain of a multi-grain table (data warehousing). The grain filter can be ignored when joining to a multi-grain table using the primary key
    """

    def __init__(self):


class DynaFunction(Operation):

    def __init__(self, name:str, parameters:list[RelationalOperationElement]=[]):
        self.name = name
        self.parameters = parameters


class ColumnName(RelationalOperationElement):

    def __init__(self, name:str):
        self.name = name


class RelationalTds(Any):

    def __init__(self, paths:list[Pair]=[]):
        self.paths = paths


class PathInformation(Any):

    def __init__(self, type:Type, propertyMapping:PropertyMapping=None, documentation:str=None, relationalType:DataType=None):
        self.type = type
        self.propertyMapping = propertyMapping
        self.documentation = documentation
        self.relationalType = relationalType


class TableAliasColumn(RelationalOperationElement):

    def __init__(self, alias:TableAlias, column:Column, setMappingOwner:PropertyMappingsImplementation=None, columnName:str=None):
        self.alias = alias
        self.column = column
        self.setMappingOwner = setMappingOwner
        self.columnName = columnName


class RelationalOperationElementWithJoin(RelationalOperationElement):

    def __init__(self, relationalOperationElement:RelationalOperationElement=None, joinTreeNode:JoinTreeNode=None):
        self.relationalOperationElement = relationalOperationElement
        self.joinTreeNode = joinTreeNode


class Literal(RelationalOperationElement):

    def __init__(self, value:Any):
        self.value = value


class LiteralList(RelationalOperationElement):

    def __init__(self, values:list[Literal]=[]):
        self.values = values


class SQLNull(Any):

    def __init__(self, toString:str, key:Nil=None):
        self.toString = toString
        self.key = key


class OrderBy(Any):

    def __init__(self, column:RelationalOperationElement, direction:SortDirection):
        self.column = column
        self.direction = direction


class Pivot(Any):

    def __init__(self, pivotColumns:list[RelationalOperationElement]=[], aggColumns:list[RelationalOperationElement]=[]):
        self.pivotColumns = pivotColumns
        self.aggColumns = aggColumns


class WindowColumn(RelationalOperationElement):

    def __init__(self, columnName:str, window:Window, func:DynaFunction):
        self.columnName = columnName
        self.window = window
        self.func = func


class Window(RelationalOperationElement):

    def __init__(self, partition:list[RelationalOperationElement]=[], sortBy:list[RelationalOperationElement]=[], sortDirection:SortDirection=None):
        self.partition = partition
        self.sortBy = sortBy
        self.sortDirection = sortDirection


class SortDirection(Enum):
    ASC = auto()
    DESC = auto()

class TableAliasColumnName(RelationalOperationElement):

    def __init__(self, alias:TableAlias, columnName:str):
        self.alias = alias
        self.columnName = columnName


class UpsertSQLQuery(SQLQuery):

    def __init__(self, data:Table, equalityStatements:Map):
        self.data = data
        self.equalityStatements = equalityStatements


class RelationDataSelectSqlQuery(SelectSQLQuery):

    def __init__(self, relation:NamedRelation, columnSubset:list[Column]=[]):
        self.relation = relation
        self.columnSubset = columnSubset


class RelationData(Any):

    def __init__(self, relation:NamedRelation, schema:Schema, database:Database, columnSubset:list[Column]=[], rows:list[DataRow]=[]):
        self.relation = relation
        self.schema = schema
        self.database = database
        self.columnSubset = columnSubset
        self.rows = rows


class DataRow(Any):

    def __init__(self, values:list[Any]=[]):
        self.values = values


class CreateSchemaSQL(SQLQuery):

    def __init__(self, schema:Schema):
        self.schema = schema


class DropSchemaSQL(SQLQuery):

    def __init__(self, schema:Schema):
        self.schema = schema


class CreateTableSQL(SQLQuery):

    def __init__(self, table:Table, applyConstraints:bool=None, isTempTable:bool=None):
        self.table = table
        self.applyConstraints = applyConstraints
        self.isTempTable = isTempTable


class DropTableSQL(SQLQuery):

    def __init__(self, table:Table):
        self.table = table


class LoadTableSQL(SQLQuery):

    def __init__(self, table:Table, columnsToLoad:list[Column]=[], parsedData:List=None, absolutePathToFile:VarPlaceHolder=None):
        self.table = table
        self.columnsToLoad = columnsToLoad
        self.parsedData = parsedData
        self.absolutePathToFile = absolutePathToFile


class Alterable(Any):

    def __init__(self):


class Session(Alterable):

    def __init__(self):


class AlterSQL(SQLQuery):

    def __init__(self, object:Alterable, operation:list[AlterOperation]=[]):
        self.object = object
        self.operation = operation


class AlterOperation(Any):

    def __init__(self):


class SetOperation(AlterOperation):

    def __init__(self, propertyName:str, propertyValue:Literal):
        self.propertyName = propertyName
        self.propertyValue = propertyValue


class UnSetOperation(AlterOperation):

    def __init__(self, propertyName:str):
        self.propertyName = propertyName


class RelationalMapper(PackageableElement,PostProcessorParameter):

    def __init__(self, databaseMappers:list[DatabaseMapper]=[], schemaMappers:list[SchemaMapper]=[], tableMappers:list[TableMapper]=[]):
        self.databaseMappers = databaseMappers
        self.schemaMappers = schemaMappers
        self.tableMappers = tableMappers


class DatabaseMapper(Any):

    def __init__(self, database:str, schemas:list[Schema]=[]):
        self.database = database
        self.schemas = schemas


class SchemaMapper(Any):

    def __init__(self, from:Schema, to:str):
        self.from = from
        self.to = to


class TableMapper(Any):

    def __init__(self, from:Table, to:str):
        self.from = from
        self.to = to

meta/relational/metamodel/relation


class Relation(RelationalOperationElement,SetRelation):

    def __init__(self, columns:list[RelationalOperationElement]=[]):
        self.columns = columns


class NamedRelation(Relation):

    def __init__(self, name:str):
        self.name = name


class Milestoning(Any):

    def __init__(self, owner:Relation=None):
        self.owner = owner


class TemporalMilestoning(Milestoning):

    def __init__(self, infinityDate:Date=None):
        self.infinityDate = infinityDate


class ProcessingMilestoning(TemporalMilestoning):

    def __init__(self, in:Column, out:Column, outIsInclusive:bool):
        self.in = in
        self.out = out
        self.outIsInclusive = outIsInclusive


class BusinessMilestoning(TemporalMilestoning):

    def __init__(self, from:Column, thru:Column, thruIsInclusive:bool):
        self.from = from
        self.thru = thru
        self.thruIsInclusive = thruIsInclusive


class BusinessSnapshotMilestoning(TemporalMilestoning):

    def __init__(self, snapshotDate:Column):
        self.snapshotDate = snapshotDate


class Table(NamedRelation):

    def __init__(self, schema:Schema, primaryKey:list[Column]=[], milestoning:list[Milestoning]=[], temporaryTable:bool=None):
        self.schema = schema
        self.primaryKey = primaryKey
        self.milestoning = milestoning
        self.temporaryTable = temporaryTable


class View(NamedRelation,RelationalMappingSpecification):

    def __init__(self, schema:Schema, primaryKey:list[Column]=[], columnMappings:list[ColumnMapping]=[]):
        self.schema = schema
        self.primaryKey = primaryKey
        self.columnMappings = columnMappings


class TabularFunction(NamedRelation):

    def __init__(self, schema:Schema):
        self.schema = schema


class SelectSQLQuery(Relation,SQLQuery):

    def __init__(self, distinct:bool=None, data:RootJoinTreeNode=None, filteringOperation:list[RelationalOperationElement]=[], groupBy:list[RelationalOperationElement]=[], pivot:Pivot=None, havingOperation:list[RelationalOperationElement]=[], orderBy:list[OrderBy]=[], fromRow:Literal=None, toRow:Literal=None, leftSideOfFilter:RelationalTreeNode=None, savedFilteringOperation:list[Pair]=[], extraFilteringOperation:list[RelationalOperationElement]=[], preIsolationCurrentTreeNode:RelationalTreeNode=None):
        self.distinct = distinct
        self.data = data
        self.filteringOperation = filteringOperation
        self.groupBy = groupBy
        self.pivot = pivot
        self.havingOperation = havingOperation
        self.orderBy = orderBy
        self.fromRow = fromRow
        self.toRow = toRow
        self.leftSideOfFilter = leftSideOfFilter
        self.savedFilteringOperation = savedFilteringOperation
        self.extraFilteringOperation = extraFilteringOperation
        self.preIsolationCurrentTreeNode = preIsolationCurrentTreeNode


class ViewSelectSQLQuery(Table):

    def __init__(self, selectSQLQuery:SelectSQLQuery, view:View):
        self.selectSQLQuery = selectSQLQuery
        self.view = view


class TdsSelectSqlQuery(SelectSQLQuery,RelationalTds):

    def __init__(self):


class TableTds(RelationalTds):

    def __init__(self):


class SemiStructuredArrayFlatten(Relation):

    def __init__(self, navigation:RelationalOperationElement):
        self.navigation = navigation


class SemiStructuredArrayFlattenOutput(RelationalOperationElement):

    def __init__(self, tableAliasColumn:TableAliasColumn, returnType:Type=None):
        self.tableAliasColumn = tableAliasColumn
        self.returnType = returnType


class Union(Relation):

    def __init__(self, currentTreeNodes:list[RelationalTreeNode]=[], setImplementations:list[SetImplementation]=[], queries:list[SelectSQLQuery]=[]):
        self.currentTreeNodes = currentTreeNodes
        self.setImplementations = setImplementations
        self.queries = queries


class UnionAll(Union):

    def __init__(self):


class TdsSelectSQLQueryWithCommonTableExpressions(TdsSelectSqlQuery,SelectSQLQueryWithCommonTableExpressions):

    def __init__(self):


class SelectSQLQueryWithCommonTableExpressions(SelectSQLQuery):

    def __init__(self, commonTableExpressions:list[CommonTableExpression]=[]):
        self.commonTableExpressions = commonTableExpressions


class CommonTableExpression(RelationalOperationElement):

    def __init__(self, name:str, sqlQuery:SQLQuery):
        self.name = name
        self.sqlQuery = sqlQuery


class SelectCommonTableExpression(Relation,CommonTableExpression):

    def __init__(self, selectSQLQuery:SelectSQLQuery, materialized:bool=None):
        self.selectSQLQuery = selectSQLQuery
        self.materialized = materialized


class CommonTableExpressionReference(RelationalOperationElement):

    def __init__(self, name:str):
        self.name = name


meta/relational/metamodel/join


class RelationalTreeNode(TreeNode):

    def __init__(self, alias:TableAlias):
        self.alias = alias


class RootJoinTreeNode(RelationalTreeNode,Relation):

    def __init__(self):


class JoinTreeNode(RelationalTreeNode):

    def __init__(self, database:Database, joinName:str, join:Join, setMappingOwner:PropertyMappingsImplementation=None, joinType:JoinType=None, lateral:bool=None):
        self.database = database
        self.joinName = joinName
        self.join = join
        self.setMappingOwner = setMappingOwner
        self.joinType = joinType
        self.lateral = lateral


class Join(Any):

    def __init__(self, name:str, operation:Operation, database:Database=None, target:TableAlias=None, aliases:list[Pair]=[]):
        self.name = name
        self.operation = operation
        self.database = database
        self.target = target
        self.aliases = aliases


class AsOfJoin(Join):

    def __init__(self):


class JoinType(Enum):
    INNER = auto()
    LEFT_OUTER = auto()
    RIGHT_OUTER = auto()
    FULL_OUTER = auto()

meta/relational/metamodel/operation


class Function(RelationalOperationElement):

    def __init__(self):


class Operation(Function):

    def __init__(self):


class BinaryOperation(Operation):

    def __init__(self, left:RelationalOperationElement, right:RelationalOperationElement):
        self.left = left
        self.right = right


class UnaryOperation(Operation):

    def __init__(self, nested:RelationalOperationElement):
        self.nested = nested


class VariableArityOperation(Operation):

    def __init__(self, args:list[RelationalOperationElement]=[]):
        self.args = args


class JoinStrings(Operation):

    def __init__(self, strings:list[RelationalOperationElement]=[], prefix:RelationalOperationElement=None, separator:RelationalOperationElement=None, suffix:RelationalOperationElement=None):
        self.strings = strings
        self.prefix = prefix
        self.separator = separator
        self.suffix = suffix


class ArithmeticOperation(Operation):

    def __init__(self):


class VariableArithmeticOperation(ArithmeticOperation,VariableArityOperation):

    def __init__(self):


class SemiStructuredObjectNavigation(Operation):

    def __init__(self, operand:RelationalOperationElement, contentType:str=None, returnType:Type=None, avoidCastIfPrimitive:bool=None):
        self.operand = operand
        self.contentType = contentType
        self.returnType = returnType
        self.avoidCastIfPrimitive = avoidCastIfPrimitive


class SemiStructuredPropertyAccess(SemiStructuredObjectNavigation):

    def __init__(self, property:RelationalOperationElement, index:RelationalOperationElement=None):
        self.property = property
        self.index = index


class SemiStructuredArrayElementAccess(SemiStructuredObjectNavigation):

    def __init__(self, index:RelationalOperationElement):
        self.index = index


meta/relational/metamodel/datatype


class DataType(Any):

    def __init__(self):


class CoreDataType(DataType):

    def __init__(self):


class DbSpecificDataType(DataType):

    def __init__(self, coreDataType:CoreDataType, dbSpecificSql:str):
        self.coreDataType = coreDataType
        self.dbSpecificSql = dbSpecificSql


class BigInt(CoreDataType):

    def __init__(self):


class SmallInt(CoreDataType):

    def __init__(self):


class TinyInt(CoreDataType):

    def __init__(self):


class Integer(CoreDataType):

    def __init__(self):


class Float(CoreDataType):

    def __init__(self):


class Double(CoreDataType):

    def __init__(self):


class Varchar(CoreDataType):

    def __init__(self, size:int):
        self.size = size


class Char(CoreDataType):

    def __init__(self, size:int):
        self.size = size


class Varbinary(CoreDataType):

    def __init__(self, size:int):
        self.size = size


class Decimal(CoreDataType):

    def __init__(self, precision:int, scale:int):
        self.precision = precision
        self.scale = scale


class Numeric(CoreDataType):

    def __init__(self, precision:int, scale:int):
        self.precision = precision
        self.scale = scale


class Timestamp(CoreDataType):

    def __init__(self):


class Date(CoreDataType):

    def __init__(self):


class Distinct(CoreDataType):

    def __init__(self):


class Other(CoreDataType):

    def __init__(self):


class Bit(CoreDataType):

    def __init__(self):


class Binary(CoreDataType):

    def __init__(self, size:int):
        self.size = size


class Real(CoreDataType):

    def __init__(self):


class Array(CoreDataType):

    def __init__(self):


class SemiStructured(CoreDataType):

    def __init__(self):


class Json(CoreDataType):
    """SingleStore JSON type
    """

    def __init__(self):


meta/relational/metamodel/execute


class ResultSet(Any):

    def __init__(self, executionTimeInNanoSecond:int, connectionAcquisitionTimeInNanoSecond:int, executionPlanInformation:str=None, columnNames:list[str]=[], rows:list[Row]=[], dataSource:DataSource=None):
        self.executionTimeInNanoSecond = executionTimeInNanoSecond
        self.connectionAcquisitionTimeInNanoSecond = connectionAcquisitionTimeInNanoSecond
        self.executionPlanInformation = executionPlanInformation
        self.columnNames = columnNames
        self.rows = rows
        self.dataSource = dataSource


class Row(Any):

    def __init__(self, parent:ResultSet, value:Any, values:list[Any]=[]):
        self.parent = parent
        self.value = value
        self.values = values

meta/relational/metamodel/execute/tests


meta/relational/metamodel/data


class RelationalCSVData(EmbeddedData):

    def __init__(self, tables:list[RelationalCSVTable]=[]):
        self.tables = tables


class RelationalCSVTable(Any):

    def __init__(self, schema:str, table:str, values:str):
        self.schema = schema
        self.table = table
        self.values = values


meta/relational/metamodel/assertion
