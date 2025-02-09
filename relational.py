meta/relational/metamodel


class Database(SetBasedStore):

    def __init__(self, namespaces:list[Namespace]=[], includes:list[Store]=[], package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], schemas:list[Schema]=[], joins:list[Join]=[], filters:list[Filter]=[]):
        super().__init__(namespaces,includes,package,name,stereotypes,taggedValues,referenceUsages)
        self.schemas = schemas
        self.joins = joins
        self.filters = filters


class Schema(Namespace):

    def __init__(self, name:str, database:Database, relations:list[SetRelation]=[], tables:list[Table]=[], views:list[View]=[], tabularFunctions:list[TabularFunction]=[]):
        super().__init__(relations)
        self.name = name
        self.database = database
        self.tables = tables
        self.views = views
        self.tabularFunctions = tabularFunctions


class RelationalMappingSpecification():

    def __init__(self, userDefinedPrimaryKey:bool, mainTableAlias:TableAlias, filter:FilterMapping=None, distinct:bool=None, groupBy:GroupByMapping=None):
        self.userDefinedPrimaryKey = userDefinedPrimaryKey
        self.mainTableAlias = mainTableAlias
        self.filter = filter
        self.distinct = distinct
        self.groupBy = groupBy


class Filter():

    def __init__(self, name:str, operation:Operation, database:Database=None):
        self.name = name
        self.operation = operation
        self.database = database


class Alias(RelationalOperationElement):

    def __init__(self, name:str, relationalElement:RelationalOperationElement):
        super().__init__()
        self.name = name
        self.relationalElement = relationalElement


class SQLQuery(RelationalOperationElement):

    def __init__(self, comment:str=None):
        super().__init__()
        self.comment = comment


class TableAlias(Alias):

    def __init__(self, name:str, relationalElement:RelationalOperationElement, setMappingOwner:PropertyMappingsImplementation=None, database:Database=None, schema:str=None):
        super().__init__(name,relationalElement)
        self.setMappingOwner = setMappingOwner
        self.database = database
        self.schema = schema


class Column(RelationalOperationElement,SetColumn):

    def __init__(self, name:str, type:DataType, nullable:bool=None, owner:Relation=None):
        RelationalOperationElement.__init__()
        SetColumn.__init__()
        self.name = name
        self.type = type
        self.nullable = nullable
        self.owner = owner


class RelationalOperationElement():

    def __init__(self):
        pass

class MultiGrainFilter(Filter):
    """Indicates that the filter is a filter on the grain of a multi-grain table (data warehousing). The grain filter can be ignored when joining to a multi-grain table using the primary key
    """

    def __init__(self, name:str, operation:Operation, database:Database=None):
        super().__init__(name,operation,database)


class DynaFunction(Operation):

    def __init__(self, name:str, parameters:list[RelationalOperationElement]=[]):
        super().__init__()
        self.name = name
        self.parameters = parameters


class ColumnName(RelationalOperationElement):

    def __init__(self, name:str):
        super().__init__()
        self.name = name


class RelationalTds():

    def __init__(self, paths:list[Pair]=[]):
        self.paths = paths


class PathInformation():

    def __init__(self, type:Type, propertyMapping:PropertyMapping=None, documentation:str=None, relationalType:DataType=None):
        self.type = type
        self.propertyMapping = propertyMapping
        self.documentation = documentation
        self.relationalType = relationalType


class TableAliasColumn(RelationalOperationElement):

    def __init__(self, alias:TableAlias, column:Column, setMappingOwner:PropertyMappingsImplementation=None, columnName:str=None):
        super().__init__()
        self.alias = alias
        self.column = column
        self.setMappingOwner = setMappingOwner
        self.columnName = columnName


class RelationalOperationElementWithJoin(RelationalOperationElement):

    def __init__(self, relationalOperationElement:RelationalOperationElement=None, joinTreeNode:JoinTreeNode=None):
        super().__init__()
        self.relationalOperationElement = relationalOperationElement
        self.joinTreeNode = joinTreeNode


class Literal(RelationalOperationElement):

    def __init__(self, value:Any):
        super().__init__()
        self.value = value


class LiteralList(RelationalOperationElement):

    def __init__(self, values:list[Literal]=[]):
        super().__init__()
        self.values = values


class SQLNull():

    def __init__(self, key:Nil=None):
        self.key = key


class OrderBy():

    def __init__(self, column:RelationalOperationElement, direction:SortDirection):
        self.column = column
        self.direction = direction


class Pivot():

    def __init__(self, pivotColumns:list[RelationalOperationElement]=[], aggColumns:list[RelationalOperationElement]=[]):
        self.pivotColumns = pivotColumns
        self.aggColumns = aggColumns


class WindowColumn(RelationalOperationElement):

    def __init__(self, columnName:str, window:Window, func:DynaFunction):
        super().__init__()
        self.columnName = columnName
        self.window = window
        self.func = func


class Window(RelationalOperationElement):

    def __init__(self, partition:list[RelationalOperationElement]=[], sortBy:list[RelationalOperationElement]=[], sortDirection:SortDirection=None):
        super().__init__()
        self.partition = partition
        self.sortBy = sortBy
        self.sortDirection = sortDirection


class SortDirection(Enum):
    ASC = auto()
    DESC = auto()

class TableAliasColumnName(RelationalOperationElement):

    def __init__(self, alias:TableAlias, columnName:str):
        super().__init__()
        self.alias = alias
        self.columnName = columnName


class UpsertSQLQuery(SQLQuery):

    def __init__(self, data:Table, equalityStatements:Map, comment:str=None):
        super().__init__(comment)
        self.data = data
        self.equalityStatements = equalityStatements


class RelationDataSelectSqlQuery(SelectSQLQuery):

    def __init__(self, relation:NamedRelation, distinct:bool=None, data:RootJoinTreeNode=None, filteringOperation:list[RelationalOperationElement]=[], groupBy:list[RelationalOperationElement]=[], pivot:Pivot=None, havingOperation:list[RelationalOperationElement]=[], orderBy:list[OrderBy]=[], fromRow:Literal=None, toRow:Literal=None, leftSideOfFilter:RelationalTreeNode=None, savedFilteringOperation:list[Pair]=[], extraFilteringOperation:list[RelationalOperationElement]=[], preIsolationCurrentTreeNode:RelationalTreeNode=None, columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[], comment:str=None, columnSubset:list[Column]=[]):
        super().__init__(distinct,data,filteringOperation,groupBy,pivot,havingOperation,orderBy,fromRow,toRow,leftSideOfFilter,savedFilteringOperation,extraFilteringOperation,preIsolationCurrentTreeNode,columns,setColumns,comment)
        self.relation = relation
        self.columnSubset = columnSubset


class RelationData():

    def __init__(self, relation:NamedRelation, columnSubset:list[Column]=[], rows:list[DataRow]=[]):
        self.relation = relation
        self.columnSubset = columnSubset
        self.rows = rows


class DataRow():

    def __init__(self, values:list[Any]=[]):
        self.values = values


class CreateSchemaSQL(SQLQuery):

    def __init__(self, schema:Schema, comment:str=None):
        super().__init__(comment)
        self.schema = schema


class DropSchemaSQL(SQLQuery):

    def __init__(self, schema:Schema, comment:str=None):
        super().__init__(comment)
        self.schema = schema


class CreateTableSQL(SQLQuery):

    def __init__(self, table:Table, comment:str=None, applyConstraints:bool=None, isTempTable:bool=None):
        super().__init__(comment)
        self.table = table
        self.applyConstraints = applyConstraints
        self.isTempTable = isTempTable


class DropTableSQL(SQLQuery):

    def __init__(self, table:Table, comment:str=None):
        super().__init__(comment)
        self.table = table


class LoadTableSQL(SQLQuery):

    def __init__(self, table:Table, comment:str=None, columnsToLoad:list[Column]=[], parsedData:List=None, absolutePathToFile:VarPlaceHolder=None):
        super().__init__(comment)
        self.table = table
        self.columnsToLoad = columnsToLoad
        self.parsedData = parsedData
        self.absolutePathToFile = absolutePathToFile


class Alterable():

    def __init__(self):
        pass

class Session(Alterable):

    def __init__(self):
        super().__init__()


class AlterSQL(SQLQuery):

    def __init__(self, object:Alterable, comment:str=None, operation:list[AlterOperation]=[]):
        super().__init__(comment)
        self.object = object
        self.operation = operation


class AlterOperation():

    def __init__(self):
        pass

class SetOperation(AlterOperation):

    def __init__(self, propertyName:str, propertyValue:Literal):
        super().__init__()
        self.propertyName = propertyName
        self.propertyValue = propertyValue


class UnSetOperation(AlterOperation):

    def __init__(self, propertyName:str):
        super().__init__()
        self.propertyName = propertyName


class RelationalMapper(PackageableElement,PostProcessorParameter):

    def __init__(self, package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], databaseMappers:list[DatabaseMapper]=[], schemaMappers:list[SchemaMapper]=[], tableMappers:list[TableMapper]=[]):
        PackageableElement.__init__(package,name,stereotypes,taggedValues,referenceUsages)
        PostProcessorParameter.__init__()
        self.databaseMappers = databaseMappers
        self.schemaMappers = schemaMappers
        self.tableMappers = tableMappers


class DatabaseMapper():

    def __init__(self, database:str, schemas:list[Schema]=[]):
        self.database = database
        self.schemas = schemas


class SchemaMapper():

    def __init__(self, from:Schema, to:str):
        self.from = from
        self.to = to


class TableMapper():

    def __init__(self, from:Table, to:str):
        self.from = from
        self.to = to

meta/relational/metamodel/relation


class Relation(RelationalOperationElement,SetRelation):

    def __init__(self, setColumns:list[SetColumn]=[], columns:list[RelationalOperationElement]=[]):
        RelationalOperationElement.__init__()
        SetRelation.__init__(setColumns)
        self.columns = columns


class NamedRelation(Relation):

    def __init__(self, name:str, columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[]):
        super().__init__(columns,setColumns)
        self.name = name


class Milestoning():

    def __init__(self, owner:Relation=None):
        self.owner = owner


class TemporalMilestoning(Milestoning):

    def __init__(self, owner:Relation=None, infinityDate:datetime.datetime=None):
        super().__init__(owner)
        self.infinityDate = infinityDate


class ProcessingMilestoning(TemporalMilestoning):

    def __init__(self, in:Column, out:Column, outIsInclusive:bool, infinityDate:datetime.datetime=None, owner:Relation=None):
        super().__init__(infinityDate,owner)
        self.in = in
        self.out = out
        self.outIsInclusive = outIsInclusive


class BusinessMilestoning(TemporalMilestoning):

    def __init__(self, from:Column, thru:Column, thruIsInclusive:bool, infinityDate:datetime.datetime=None, owner:Relation=None):
        super().__init__(infinityDate,owner)
        self.from = from
        self.thru = thru
        self.thruIsInclusive = thruIsInclusive


class BusinessSnapshotMilestoning(TemporalMilestoning):

    def __init__(self, snapshotDate:Column, infinityDate:datetime.datetime=None, owner:Relation=None):
        super().__init__(infinityDate,owner)
        self.snapshotDate = snapshotDate


class Table(NamedRelation):

    def __init__(self, name:str, schema:Schema, columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[], primaryKey:list[Column]=[], milestoning:list[Milestoning]=[], temporaryTable:bool=None):
        super().__init__(name,columns,setColumns)
        self.schema = schema
        self.primaryKey = primaryKey
        self.milestoning = milestoning
        self.temporaryTable = temporaryTable


class View(NamedRelation,RelationalMappingSpecification):

    def __init__(self, name:str, userDefinedPrimaryKey:bool, mainTableAlias:TableAlias, schema:Schema, columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[], filter:FilterMapping=None, distinct:bool=None, groupBy:GroupByMapping=None, primaryKey:list[Column]=[], columnMappings:list[ColumnMapping]=[]):
        NamedRelation.__init__(name,columns,setColumns)
        RelationalMappingSpecification.__init__(userDefinedPrimaryKey,mainTableAlias,filter,distinct,groupBy)
        self.schema = schema
        self.primaryKey = primaryKey
        self.columnMappings = columnMappings


class TabularFunction(NamedRelation):

    def __init__(self, name:str, schema:Schema, columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[]):
        super().__init__(name,columns,setColumns)
        self.schema = schema


class SelectSQLQuery(Relation,SQLQuery):

    def __init__(self, columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[], comment:str=None, distinct:bool=None, data:RootJoinTreeNode=None, filteringOperation:list[RelationalOperationElement]=[], groupBy:list[RelationalOperationElement]=[], pivot:Pivot=None, havingOperation:list[RelationalOperationElement]=[], orderBy:list[OrderBy]=[], fromRow:Literal=None, toRow:Literal=None, leftSideOfFilter:RelationalTreeNode=None, savedFilteringOperation:list[Pair]=[], extraFilteringOperation:list[RelationalOperationElement]=[], preIsolationCurrentTreeNode:RelationalTreeNode=None):
        Relation.__init__(columns,setColumns)
        SQLQuery.__init__(comment)
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

    def __init__(self, schema:Schema, name:str, selectSQLQuery:SelectSQLQuery, view:View, primaryKey:list[Column]=[], milestoning:list[Milestoning]=[], temporaryTable:bool=None, columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[]):
        super().__init__(schema,name,primaryKey,milestoning,temporaryTable,columns,setColumns)
        self.selectSQLQuery = selectSQLQuery
        self.view = view


class TdsSelectSqlQuery(SelectSQLQuery,RelationalTds):

    def __init__(self, distinct:bool=None, data:RootJoinTreeNode=None, filteringOperation:list[RelationalOperationElement]=[], groupBy:list[RelationalOperationElement]=[], pivot:Pivot=None, havingOperation:list[RelationalOperationElement]=[], orderBy:list[OrderBy]=[], fromRow:Literal=None, toRow:Literal=None, leftSideOfFilter:RelationalTreeNode=None, savedFilteringOperation:list[Pair]=[], extraFilteringOperation:list[RelationalOperationElement]=[], preIsolationCurrentTreeNode:RelationalTreeNode=None, columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[], comment:str=None, paths:list[Pair]=[]):
        SelectSQLQuery.__init__(distinct,data,filteringOperation,groupBy,pivot,havingOperation,orderBy,fromRow,toRow,leftSideOfFilter,savedFilteringOperation,extraFilteringOperation,preIsolationCurrentTreeNode,columns,setColumns,comment)
        RelationalTds.__init__(paths)


class TableTds(RelationalTds):

    def __init__(self, paths:list[Pair]=[]):
        super().__init__(paths)


class SemiStructuredArrayFlatten(Relation):

    def __init__(self, navigation:RelationalOperationElement, columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[]):
        super().__init__(columns,setColumns)
        self.navigation = navigation


class SemiStructuredArrayFlattenOutput(RelationalOperationElement):

    def __init__(self, tableAliasColumn:TableAliasColumn, returnType:Type=None):
        super().__init__()
        self.tableAliasColumn = tableAliasColumn
        self.returnType = returnType


class Union(Relation):

    def __init__(self, columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[], currentTreeNodes:list[RelationalTreeNode]=[], setImplementations:list[SetImplementation]=[], queries:list[SelectSQLQuery]=[]):
        super().__init__(columns,setColumns)
        self.currentTreeNodes = currentTreeNodes
        self.setImplementations = setImplementations
        self.queries = queries


class UnionAll(Union):

    def __init__(self, currentTreeNodes:list[RelationalTreeNode]=[], setImplementations:list[SetImplementation]=[], queries:list[SelectSQLQuery]=[], columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[]):
        super().__init__(currentTreeNodes,setImplementations,queries,columns,setColumns)


class TdsSelectSQLQueryWithCommonTableExpressions(TdsSelectSqlQuery,SelectSQLQueryWithCommonTableExpressions):

    def __init__(self, distinct:bool=None, data:RootJoinTreeNode=None, filteringOperation:list[RelationalOperationElement]=[], groupBy:list[RelationalOperationElement]=[], pivot:Pivot=None, havingOperation:list[RelationalOperationElement]=[], orderBy:list[OrderBy]=[], fromRow:Literal=None, toRow:Literal=None, leftSideOfFilter:RelationalTreeNode=None, savedFilteringOperation:list[Pair]=[], extraFilteringOperation:list[RelationalOperationElement]=[], preIsolationCurrentTreeNode:RelationalTreeNode=None, columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[], comment:str=None, paths:list[Pair]=[], commonTableExpressions:list[CommonTableExpression]=[]):
        TdsSelectSqlQuery.__init__(distinct,data,filteringOperation,groupBy,pivot,havingOperation,orderBy,fromRow,toRow,leftSideOfFilter,savedFilteringOperation,extraFilteringOperation,preIsolationCurrentTreeNode,columns,setColumns,comment,paths)
        SelectSQLQueryWithCommonTableExpressions.__init__(commonTableExpressions,distinct,data,filteringOperation,groupBy,pivot,havingOperation,orderBy,fromRow,toRow,leftSideOfFilter,savedFilteringOperation,extraFilteringOperation,preIsolationCurrentTreeNode,columns,setColumns,comment)


class SelectSQLQueryWithCommonTableExpressions(SelectSQLQuery):

    def __init__(self, distinct:bool=None, data:RootJoinTreeNode=None, filteringOperation:list[RelationalOperationElement]=[], groupBy:list[RelationalOperationElement]=[], pivot:Pivot=None, havingOperation:list[RelationalOperationElement]=[], orderBy:list[OrderBy]=[], fromRow:Literal=None, toRow:Literal=None, leftSideOfFilter:RelationalTreeNode=None, savedFilteringOperation:list[Pair]=[], extraFilteringOperation:list[RelationalOperationElement]=[], preIsolationCurrentTreeNode:RelationalTreeNode=None, columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[], comment:str=None, commonTableExpressions:list[CommonTableExpression]=[]):
        super().__init__(distinct,data,filteringOperation,groupBy,pivot,havingOperation,orderBy,fromRow,toRow,leftSideOfFilter,savedFilteringOperation,extraFilteringOperation,preIsolationCurrentTreeNode,columns,setColumns,comment)
        self.commonTableExpressions = commonTableExpressions


class CommonTableExpression(RelationalOperationElement):

    def __init__(self, name:str, sqlQuery:SQLQuery):
        super().__init__()
        self.name = name
        self.sqlQuery = sqlQuery


class SelectCommonTableExpression(Relation,CommonTableExpression):

    def __init__(self, name:str, sqlQuery:SQLQuery, columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[], materialized:bool=None):
        Relation.__init__(columns,setColumns)
        CommonTableExpression.__init__(name,sqlQuery)
        self.materialized = materialized


class CommonTableExpressionReference(RelationalOperationElement):

    def __init__(self, name:str):
        super().__init__()
        self.name = name


meta/relational/metamodel/join


class RelationalTreeNode(TreeNode):

    def __init__(self, alias:TableAlias, childrenData:list[TreeNode]=[]):
        super().__init__(childrenData)
        self.alias = alias


class RootJoinTreeNode(RelationalTreeNode,Relation):

    def __init__(self, alias:TableAlias, childrenData:list[TreeNode]=[], columns:list[RelationalOperationElement]=[], setColumns:list[SetColumn]=[]):
        RelationalTreeNode.__init__(alias,childrenData)
        Relation.__init__(columns,setColumns)


class JoinTreeNode(RelationalTreeNode):

    def __init__(self, alias:TableAlias, database:Database, joinName:str, join:Join, childrenData:list[TreeNode]=[], setMappingOwner:PropertyMappingsImplementation=None, joinType:JoinType=None, lateral:bool=None):
        super().__init__(alias,childrenData)
        self.database = database
        self.joinName = joinName
        self.join = join
        self.setMappingOwner = setMappingOwner
        self.joinType = joinType
        self.lateral = lateral


class Join():

    def __init__(self, name:str, operation:Operation, database:Database=None, target:TableAlias=None, aliases:list[Pair]=[]):
        self.name = name
        self.operation = operation
        self.database = database
        self.target = target
        self.aliases = aliases


class AsOfJoin(Join):

    def __init__(self, name:str, operation:Operation, database:Database=None, target:TableAlias=None, aliases:list[Pair]=[]):
        super().__init__(name,operation,database,target,aliases)


class JoinType(Enum):
    INNER = auto()
    LEFT_OUTER = auto()
    RIGHT_OUTER = auto()
    FULL_OUTER = auto()

meta/relational/metamodel/operation


class Function(RelationalOperationElement):

    def __init__(self):
        super().__init__()


class Operation(Function):

    def __init__(self):
        super().__init__()


class BinaryOperation(Operation):

    def __init__(self, left:RelationalOperationElement, right:RelationalOperationElement):
        super().__init__()
        self.left = left
        self.right = right


class UnaryOperation(Operation):

    def __init__(self, nested:RelationalOperationElement):
        super().__init__()
        self.nested = nested


class VariableArityOperation(Operation):

    def __init__(self, args:list[RelationalOperationElement]=[]):
        super().__init__()
        self.args = args


class JoinStrings(Operation):

    def __init__(self, strings:list[RelationalOperationElement]=[], prefix:RelationalOperationElement=None, separator:RelationalOperationElement=None, suffix:RelationalOperationElement=None):
        super().__init__()
        self.strings = strings
        self.prefix = prefix
        self.separator = separator
        self.suffix = suffix


class ArithmeticOperation(Operation):

    def __init__(self):
        super().__init__()


class VariableArithmeticOperation(ArithmeticOperation,VariableArityOperation):

    def __init__(self, args:list[RelationalOperationElement]=[]):
        ArithmeticOperation.__init__()
        VariableArityOperation.__init__(args)


class SemiStructuredObjectNavigation(Operation):

    def __init__(self, operand:RelationalOperationElement, contentType:str=None, returnType:Type=None, avoidCastIfPrimitive:bool=None):
        super().__init__()
        self.operand = operand
        self.contentType = contentType
        self.returnType = returnType
        self.avoidCastIfPrimitive = avoidCastIfPrimitive


class SemiStructuredPropertyAccess(SemiStructuredObjectNavigation):

    def __init__(self, operand:RelationalOperationElement, property:RelationalOperationElement, contentType:str=None, returnType:Type=None, avoidCastIfPrimitive:bool=None, index:RelationalOperationElement=None):
        super().__init__(operand,contentType,returnType,avoidCastIfPrimitive)
        self.property = property
        self.index = index


class SemiStructuredArrayElementAccess(SemiStructuredObjectNavigation):

    def __init__(self, operand:RelationalOperationElement, index:RelationalOperationElement, contentType:str=None, returnType:Type=None, avoidCastIfPrimitive:bool=None):
        super().__init__(operand,contentType,returnType,avoidCastIfPrimitive)
        self.index = index


meta/relational/metamodel/datatype


class DataType():

    def __init__(self):
        pass

class CoreDataType(DataType):

    def __init__(self):
        super().__init__()


class DbSpecificDataType(DataType):

    def __init__(self, coreDataType:CoreDataType, dbSpecificSql:str):
        super().__init__()
        self.coreDataType = coreDataType
        self.dbSpecificSql = dbSpecificSql


class BigInt(CoreDataType):

    def __init__(self):
        super().__init__()


class SmallInt(CoreDataType):

    def __init__(self):
        super().__init__()


class TinyInt(CoreDataType):

    def __init__(self):
        super().__init__()


class Integer(CoreDataType):

    def __init__(self):
        super().__init__()


class Float(CoreDataType):

    def __init__(self):
        super().__init__()


class Double(CoreDataType):

    def __init__(self):
        super().__init__()


class Varchar(CoreDataType):

    def __init__(self, size:int):
        super().__init__()
        self.size = size


class Char(CoreDataType):

    def __init__(self, size:int):
        super().__init__()
        self.size = size


class Varbinary(CoreDataType):

    def __init__(self, size:int):
        super().__init__()
        self.size = size


class Decimal(CoreDataType):

    def __init__(self, precision:int, scale:int):
        super().__init__()
        self.precision = precision
        self.scale = scale


class Numeric(CoreDataType):

    def __init__(self, precision:int, scale:int):
        super().__init__()
        self.precision = precision
        self.scale = scale


class Timestamp(CoreDataType):

    def __init__(self):
        super().__init__()


class Date(CoreDataType):

    def __init__(self):
        super().__init__()


class Distinct(CoreDataType):

    def __init__(self):
        super().__init__()


class Other(CoreDataType):

    def __init__(self):
        super().__init__()


class Bit(CoreDataType):

    def __init__(self):
        super().__init__()


class Binary(CoreDataType):

    def __init__(self, size:int):
        super().__init__()
        self.size = size


class Real(CoreDataType):

    def __init__(self):
        super().__init__()


class Array(CoreDataType):

    def __init__(self):
        super().__init__()


class SemiStructured(CoreDataType):

    def __init__(self):
        super().__init__()


class Json(CoreDataType):
    """SingleStore JSON type
    """

    def __init__(self):
        super().__init__()


meta/relational/metamodel/execute


class ResultSet():

    def __init__(self, executionTimeInNanoSecond:int, connectionAcquisitionTimeInNanoSecond:int, executionPlanInformation:str=None, columnNames:list[str]=[], rows:list[Row]=[], dataSource:DataSource=None):
        self.executionTimeInNanoSecond = executionTimeInNanoSecond
        self.connectionAcquisitionTimeInNanoSecond = connectionAcquisitionTimeInNanoSecond
        self.executionPlanInformation = executionPlanInformation
        self.columnNames = columnNames
        self.rows = rows
        self.dataSource = dataSource


class Row():

    def __init__(self, parent:ResultSet, values:list[Any]=[]):
        self.parent = parent
        self.values = values

meta/relational/metamodel/execute/tests


meta/relational/metamodel/data


class RelationalCSVData(EmbeddedData):

    def __init__(self, tables:list[RelationalCSVTable]=[]):
        super().__init__()
        self.tables = tables


class RelationalCSVTable():

    def __init__(self, schema:str, table:str, values:str):
        self.schema = schema
        self.table = table
        self.values = values


meta/relational/metamodel/assertion
