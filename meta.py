meta/pure/metamodel


class PropertyOwner(PackageableElement):

    def __init__(self):


class PackageableElement(ModelElement,Referenceable):

    def __init__(self, package:Package=None):
        self.package = package


class Referenceable(Any):

    def __init__(self, referenceUsages:list[ReferenceUsage]=[]):
        self.referenceUsages = referenceUsages


class ModelElement(AnnotatedElement):

    def __init__(self, name:str=None):
        self.name = name


class ReferenceUsage(Any):

    def __init__(self, owner:Any, propertyName:str, offset:int):
        self.owner = owner
        self.propertyName = propertyName
        self.offset = offset

meta/pure/metamodel/type


class Class(Type,PropertyOwner,ElementWithConstraints,PackageableElement,Testable):

    def __init__(self, properties:list[Property]=[], originalMilestonedProperties:list[Property]=[], propertiesFromAssociations:list[Property]=[], qualifiedProperties:list[QualifiedProperty]=[], qualifiedPropertiesFromAssociations:list[QualifiedProperty]=[], typeParameters:list[TypeParameter]=[], typeVariables:list[VariableExpression]=[], multiplicityParameters:list[InstanceValue]=[]):
        self.properties = properties
        self.originalMilestonedProperties = originalMilestonedProperties
        self.propertiesFromAssociations = propertiesFromAssociations
        self.qualifiedProperties = qualifiedProperties
        self.qualifiedPropertiesFromAssociations = qualifiedPropertiesFromAssociations
        self.typeParameters = typeParameters
        self.typeVariables = typeVariables
        self.multiplicityParameters = multiplicityParameters


class Nil(Any):

    def __init__(self):


class Any():

    def __init__(self, classifierGenericType:GenericType=None, elementOverride:ElementOverride=None):
        self.classifierGenericType = classifierGenericType
        self.elementOverride = elementOverride


class Type(Any):

    def __init__(self, name:str=None, generalizations:list[Generalization]=[], specializations:list[Generalization]=[]):
        self.name = name
        self.generalizations = generalizations
        self.specializations = specializations


class DataType(Type):

    def __init__(self):


class Measure(DataType,PackageableElement):

    def __init__(self, canonicalUnit:Unit=None, nonCanonicalUnits:list[Unit]=[]):
        self.canonicalUnit = canonicalUnit
        self.nonCanonicalUnits = nonCanonicalUnits


class Unit(DataType,Referenceable):

    def __init__(self, measure:Measure, conversionFunction:FunctionDefinition=None):
        self.measure = measure
        self.conversionFunction = conversionFunction


class PrimitiveType(DataType,PackageableElement,ElementWithConstraints):

    def __init__(self, extended:bool=None, typeVariables:list[VariableExpression]=[]):
        self.extended = extended
        self.typeVariables = typeVariables


class Enumeration(DataType,PackageableElement):

    def __init__(self, values):
        self.values = values


class Enum(AnnotatedElement):

    def __init__(self, name:str):
        self.name = name


class ElementOverride(Any):

    def __init__(self):


class GetterOverride(ElementOverride):

    def __init__(self, getterOverrideToOne:Function=None, getterOverrideToMany:Function=None, hiddenPayload:Any=None):
        self.getterOverrideToOne = getterOverrideToOne
        self.getterOverrideToMany = getterOverrideToMany
        self.hiddenPayload = hiddenPayload


class FunctionType(Type,Referenceable):

    def __init__(self, returnType:GenericType, returnMultiplicity:Multiplicity, function:list[Function]=[], parameters:list[VariableExpression]=[], typeParameters:list[TypeParameter]=[], multiplicityParameters:list[InstanceValue]=[]):
        self.returnType = returnType
        self.returnMultiplicity = returnMultiplicity
        self.function = function
        self.parameters = parameters
        self.typeParameters = typeParameters
        self.multiplicityParameters = multiplicityParameters


class ConstraintsOverride(ElementOverride):

    def __init__(self, constraintsManager:Function=None):
        self.constraintsManager = constraintsManager


class ConstraintsGetterOverride(GetterOverride,ConstraintsOverride):

    def __init__(self):


class ClassProjection(Class,PackageableElement):

    def __init__(self, projectionSpecification:RootRouteNode):
        self.projectionSpecification = projectionSpecification

meta/pure/metamodel/type/generics


class GenericType(Referenceable):

    def __init__(self, rawType:Type=None, typeParameter:TypeParameter=None, typeVariableValues:list[ValueSpecification]=[], typeArguments:list[GenericType]=[], multiplicityArguments:list[Multiplicity]=[]):
        self.rawType = rawType
        self.typeParameter = typeParameter
        self.typeVariableValues = typeVariableValues
        self.typeArguments = typeArguments
        self.multiplicityArguments = multiplicityArguments


class TypeParameter(Any):

    def __init__(self, name:str, contravariant:bool=None, lowerBound:GenericType=None, upperBound:GenericType=None):
        self.name = name
        self.contravariant = contravariant
        self.lowerBound = lowerBound
        self.upperBound = upperBound


class InferredGenericType(GenericType):

    def __init__(self):


meta/pure/metamodel/treepath


class RootRouteNode(RouteNode):

    def __init__(self, owner:Any=None):
        self.owner = owner


class RouteNode(AnnotatedElement):

    def __init__(self, name:str, includeAll:str, type:GenericType, children:list[PropertyRouteNode]=[], resolvedProperties:list[AbstractProperty]=[], included:list[RouteNodePropertyStub]=[], excluded:list[RouteNodePropertyStub]=[]):
        self.name = name
        self.includeAll = includeAll
        self.type = type
        self.children = children
        self.resolvedProperties = resolvedProperties
        self.included = included
        self.excluded = excluded


class PropertyRouteNode(RouteNode):

    def __init__(self, propertyName:str, root:RootRouteNode):
        self.propertyName = propertyName
        self.root = root


class RouteNodePropertyStub(AnnotatedElement):

    def __init__(self, owner:RouteNode, property:list[AbstractProperty]=[], parameters:list[InstanceValue]=[]):
        self.owner = owner
        self.property = property
        self.parameters = parameters


class ExistingPropertyRouteNode(PropertyRouteNode):

    def __init__(self, property:RouteNodePropertyStub):
        self.property = property


class NewPropertyRouteNode(PropertyRouteNode):

    def __init__(self, specifications:list[ValueSpecification], functionDefinition:NewPropertyRouteNodeFunctionDefinition):
        self.specifications = specifications
        self.functionDefinition = functionDefinition


class NewPropertyRouteNodeFunctionDefinition(FunctionDefinition):

    def __init__(self, owner:NewPropertyRouteNode):
        self.owner = owner


class PropertyPathTreeNode(TreeNode):

    def __init__(self, property:AbstractProperty=None, children:list[PropertyPathTreeNode]=[]):
        self.property = property
        self.children = children


meta/pure/metamodel/constraint


class Constraint(ModelElement):

    def __init__(self, functionDefinition:FunctionDefinition, owner:str=None, externalId:str=None, enforcementLevel:str=None, messageFunction:FunctionDefinition=None):
        self.functionDefinition = functionDefinition
        self.owner = owner
        self.externalId = externalId
        self.enforcementLevel = enforcementLevel
        self.messageFunction = messageFunction


class ValidatedInstance(Any):

    def __init__(self, instance:Any, results:list[ValidationResult]=[]):
        self.instance = instance
        self.results = results


class ValidationResult(Any):

    def __init__(self, success:bool, constraint:Constraint, enforcementLevel:EnforcementLevel, ins:ValidatedInstance, constraintId:str, message:str=None, inputValues:list[Pair]=[]):
        self.success = success
        self.constraint = constraint
        self.enforcementLevel = enforcementLevel
        self.ins = ins
        self.constraintId = constraintId
        self.message = message
        self.inputValues = inputValues


class ConstraintContextInformation(Any):

    def __init__(self, class:Class, constraint:Constraint, enforcementLevel:EnforcementLevel, message:str=None, messageFunction:FunctionDefinition=None):
        self.class = class
        self.constraint = constraint
        self.enforcementLevel = enforcementLevel
        self.message = message
        self.messageFunction = messageFunction


class EnforcementLevel(Enum):
    Error = auto()
    Warn = auto()

meta/pure/metamodel/function


class FunctionDefinition(Function):

    def __init__(self, expressionSequence:list[ValueSpecification]):
        self.expressionSequence = expressionSequence


class Function(Referenceable):

    def __init__(self, name:str=None, functionName:str=None, applications:list[FunctionExpression]=[]):
        self.name = name
        self.functionName = functionName
        self.applications = applications


class PackageableFunction(PackageableElement,Function):

    def __init__(self, preConstraints:list[Constraint]=[], postConstraints:list[Constraint]=[]):
        self.preConstraints = preConstraints
        self.postConstraints = postConstraints


class NativeFunction(PackageableFunction):

    def __init__(self):


class ConcreteFunctionDefinition(FunctionDefinition,PackageableFunction,Testable):

    def __init__(self):


class LambdaFunction(FunctionDefinition):

    def __init__(self, openVariables:list[str]=[]):
        self.openVariables = openVariables

meta/pure/metamodel/function/property


class Property(AbstractProperty):

    def __init__(self, aggregation:AggregationKind, defaultValue:DefaultValue=None):
        self.aggregation = aggregation
        self.defaultValue = defaultValue


class AggregationKind(Enum):
    None = auto()
    Shared = auto()
    Composite = auto()

class QualifiedProperty(AbstractProperty,FunctionDefinition):

    def __init__(self, id:str):
        self.id = id


class DefaultValue(ModelElement):

    def __init__(self, functionDefinition:FunctionDefinition=None):
        self.functionDefinition = functionDefinition


class AbstractProperty(Function,ModelElement):

    def __init__(self, genericType:GenericType, multiplicity:Multiplicity, owner:PropertyOwner):
        self.genericType = genericType
        self.multiplicity = multiplicity
        self.owner = owner


meta/pure/metamodel/relation


class GenericTypeOperationType(Enum):
    Union = auto()
    Difference = auto()
    Subset = auto()
    Equal = auto()

class GenericTypeOperation(GenericType):

    def __init__(self, left:GenericType, right:GenericType, type:GenericTypeOperationType):
        self.left = left
        self.right = right
        self.type = type


class RelationType(Type,Referenceable):

    def __init__(self, columns:list[Column]=[]):
        self.columns = columns


class Column(Function):

    def __init__(self, nameWildCard:bool):
        self.nameWildCard = nameWildCard


class Relation(Any):

    def __init__(self):


class RelationElementAccessor(Relation,Referenceable):

    def __init__(self, sourceElement:Any):
        self.sourceElement = sourceElement


class ColSpec(Any):

    def __init__(self, name:str):
        self.name = name


class ColSpecArray(Any):

    def __init__(self, names:list[str]=[]):
        self.names = names


class FuncColSpec(Any):

    def __init__(self, name:str, function:Function):
        self.name = name
        self.function = function


class FuncColSpecArray(Any):

    def __init__(self, funcSpecs:list[FuncColSpec]=[]):
        self.funcSpecs = funcSpecs


class AggColSpec(Any):

    def __init__(self, name:str, map:Function, reduce:Function):
        self.name = name
        self.map = map
        self.reduce = reduce


class AggColSpecArray(Any):

    def __init__(self, aggSpecs:list[AggColSpec]=[]):
        self.aggSpecs = aggSpecs


class TDS(Relation):

    def __init__(self, csv:str):
        self.csv = csv


class TDSRelationAccessor(RelationElementAccessor):

    def __init__(self):


meta/pure/metamodel/relationship


class Generalization(Any):

    def __init__(self, specific:Type, general:GenericType):
        self.specific = specific
        self.general = general


class Association(PropertyOwner):

    def __init__(self, properties:list[Property]=[], originalMilestonedProperties:list[Property]=[], qualifiedProperties:list[QualifiedProperty]=[]):
        self.properties = properties
        self.originalMilestonedProperties = originalMilestonedProperties
        self.qualifiedProperties = qualifiedProperties


class AssociationProjection(Association):

    def __init__(self, projections:list[ClassProjection], projectedAssociation:Association):
        self.projections = projections
        self.projectedAssociation = projectedAssociation


meta/pure/metamodel/valuespecification


class VariableExpression(Expression):

    def __init__(self, name:str, functionTypeOwner:FunctionType=None):
        self.name = name
        self.functionTypeOwner = functionTypeOwner


class InstanceValue(ValueSpecification):

    def __init__(self, values:list[Any]=[]):
        self.values = values


class ValueSpecification(Any):

    def __init__(self, genericType:GenericType, multiplicity:Multiplicity, usageContext:ValueSpecificationContext=None):
        self.genericType = genericType
        self.multiplicity = multiplicity
        self.usageContext = usageContext


class ValueSpecificationContext(Any):

    def __init__(self, offset:int):
        self.offset = offset


class Expression(ValueSpecification):

    def __init__(self):


class NonExecutableValueSpecification(ValueSpecification):

    def __init__(self, values:list[Any]=[]):
        self.values = values


class ExpressionSequenceValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, functionDefinition:FunctionDefinition):
        self.functionDefinition = functionDefinition


class InstanceValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, instanceValue:InstanceValue):
        self.instanceValue = instanceValue


class ClassConstraintValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, type:Type):
        self.type = type


class ParameterValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, functionExpression:FunctionExpression):
        self.functionExpression = functionExpression


class FunctionExpression(Expression):

    def __init__(self, func:Function, importGroup:ImportGroup, parametersValues:list[ValueSpecification]=[], functionName:str=None, propertyName:InstanceValue=None, qualifiedPropertyName:InstanceValue=None, originalMilestonedProperty:Function=None, originalMilestonedPropertyParametersValues:list[ValueSpecification]=[], resolvedTypeParameters:list[GenericType]=[], resolvedMultiplicityParameters:list[Multiplicity]=[]):
        self.func = func
        self.importGroup = importGroup
        self.parametersValues = parametersValues
        self.functionName = functionName
        self.propertyName = propertyName
        self.qualifiedPropertyName = qualifiedPropertyName
        self.originalMilestonedProperty = originalMilestonedProperty
        self.originalMilestonedPropertyParametersValues = originalMilestonedPropertyParametersValues
        self.resolvedTypeParameters = resolvedTypeParameters
        self.resolvedMultiplicityParameters = resolvedMultiplicityParameters


class KeyValueValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, functionExpression:FunctionExpression):
        self.functionExpression = functionExpression


class SimpleFunctionExpression(FunctionExpression):

    def __init__(self):


class StoreValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, store:Store):
        self.store = store


meta/pure/metamodel/multiplicity


class Multiplicity(Any):

    def __init__(self, lowerBound:MultiplicityValue=None, upperBound:MultiplicityValue=None, multiplicityParameter:str=None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.multiplicityParameter = multiplicityParameter


class MultiplicityValue(Any):

    def __init__(self, value:int=None):
        self.value = value


class PackageableMultiplicity(Multiplicity,PackageableElement):

    def __init__(self):


meta/pure/metamodel/extension


class ElementWithConstraints(Any):

    def __init__(self, constraints:list[Constraint]=[]):
        self.constraints = constraints


class ElementWithStereotypes(Any):

    def __init__(self, stereotypes:list[Stereotype]=[]):
        self.stereotypes = stereotypes


class Stereotype(Annotation):

    def __init__(self):


class ElementWithTaggedValues(Any):

    def __init__(self, taggedValues:list[TaggedValue]=[]):
        self.taggedValues = taggedValues


class TaggedValue(Any):

    def __init__(self, tag:Tag, value:str):
        self.tag = tag
        self.value = value


class AnnotatedElement(ElementWithStereotypes,ElementWithTaggedValues):

    def __init__(self):


class Profile(PackageableElement):

    def __init__(self, p_stereotypes:list[Stereotype]=[], p_tags:list[Tag]=[]):
        self.p_stereotypes = p_stereotypes
        self.p_tags = p_tags


class Tag(Annotation):

    def __init__(self):


class Annotation(Any):

    def __init__(self, profile:Profile, value:str, modelElements:list[AnnotatedElement]=[]):
        self.profile = profile
        self.value = value
        self.modelElements = modelElements


meta/pure/metamodel/import


class ImportGroup(PackageableElement):

    def __init__(self, imports:list[Import]=[]):
        self.imports = imports


class Import(Any):

    def __init__(self, path:str):
        self.path = path


class ImportStub(Any):

    def __init__(self, importGroup:ImportGroup, idOrPath:str, resolvedNode:Any=None):
        self.importGroup = importGroup
        self.idOrPath = idOrPath
        self.resolvedNode = resolvedNode


class PropertyStub(Any):

    def __init__(self, owner:Class, propertyName:str, resolvedProperty:AbstractProperty=None):
        self.owner = owner
        self.propertyName = propertyName
        self.resolvedProperty = resolvedProperty


class EnumStub(Any):

    def __init__(self, enumeration:Enumeration, enumName:str, resolvedEnum:Enum=None):
        self.enumeration = enumeration
        self.enumName = enumName
        self.resolvedEnum = resolvedEnum


meta/pure/metamodel/path


class Path(Function):

    def __init__(self, start:GenericType, path:list[PathElement]):
        self.start = start
        self.path = path


class PathElement(Any):

    def __init__(self):


class CastPathElement(PathElement):

    def __init__(self, type:GenericType):
        self.type = type


class PropertyPathElement(PathElement):

    def __init__(self, property:AbstractProperty, parameters:list[ValueSpecification]=[]):
        self.property = property
        self.parameters = parameters


meta/pure/metamodel/text


class Text(PackageableElement):

    def __init__(self, content:str, type:str=None):
        self.content = content
        self.type = type


meta/pure/metamodel/diagram


class Diagram(PackageableElement):

    def __init__(self, classViews:list[ClassView]=[], associationViews:list[AssociationView]=[], generalizationViews:list[GeneralizationView]=[], propertyViews:list[PropertyView]=[]):
        self.classViews = classViews
        self.associationViews = associationViews
        self.generalizationViews = generalizationViews
        self.propertyViews = propertyViews


class AssociationView(PropertyHolderView):

    def __init__(self, association:Association):
        self.association = association


class PropertyView(PropertyHolderView):

    def __init__(self):


class GeneralizationView(RelationshipView):

    def __init__(self):


class PropertyHolderView(RelationshipView):

    def __init__(self, property:AbstractProperty):
        self.property = property


class RelationshipView(Any):

    def __init__(self, from:RelationshipViewEnd, to:RelationshipViewEnd, path:list[Point]=[]):
        self.from = from
        self.to = to
        self.path = path


class RelationshipViewEnd(Any):

    def __init__(self, classView:ClassView):
        self.classView = classView


class ClassView(PositionedRectangle):

    def __init__(self, class:Class, id:str, hideProperties:bool=None, hideTaggedValues:bool=None, hideStereotypes:bool=None):
        self.class = class
        self.id = id
        self.hideProperties = hideProperties
        self.hideTaggedValues = hideTaggedValues
        self.hideStereotypes = hideStereotypes


class Point(Any):

    def __init__(self, x:Number, y:Number):
        self.x = x
        self.y = y


class Rectangle(Any):

    def __init__(self, width:Number, height:Number):
        self.width = width
        self.height = height


class PositionedRectangle(Any):

    def __init__(self, position:Point, rectangle:Rectangle):
        self.position = position
        self.rectangle = rectangle

meta/pure/metamodel/diagram/analytics

meta/pure/metamodel/diagram/analytics/modelCoverage


class DiagramModelCoverageAnalysisResult(Any):

    def __init__(self, classes:list[Class]=[], enumerations:list[Enumeration]=[], associations:list[Association]=[], profiles:list[Profile]=[]):
        self.classes = classes
        self.enumerations = enumerations
        self.associations = associations
        self.profiles = profiles


meta/pure/metamodel/serialization

meta/pure/metamodel/serialization/grammar


class Configuration(Any):

    def __init__(self, fullPath:bool, extensions:list[GrammarExtension]=[]):
        self.fullPath = fullPath
        self.extensions = extensions


class GrammarExtension(Any):

    def __init__(self, extraConnectionHandlers:list[Function]=[], extraInstanceValueHandlers:list[Function]=[]):
        self.extraConnectionHandlers = extraConnectionHandlers
        self.extraInstanceValueHandlers = extraInstanceValueHandlers


meta/pure/metamodel/serialization/json


class ShallowPackageableElement(Any):

    def __init__(self, package:str, name:str, sourceInformation:SourceInformation):
        self.package = package
        self.name = name
        self.sourceInformation = sourceInformation


meta/pure/metamodel/tests

meta/pure/metamodel/tests/namespace


meta/pure/metamodel/tests/lambda


class Person(Any):

    def __init__(self):


class Person2(Any):

    def __init__(self, name:str):
        self.name = name


class Employee(Person):

    def __init__(self):


class C(Any):

    def __init__(self):


class Firm(Any):

    def __init__(self, prop:str):
        self.prop = prop


meta/pure/metamodel/tests/inference


class A(Any):

    def __init__(self, val):
        self.val = val


meta/pure/metamodel/tests/functionmatching


meta/pure/metamodel/tests/lambdaopenvariables


class Person(Any):

    def __init__(self, lastName:str):
        self.lastName = lastName


class Firm(Any):

    def __init__(self, employees:list[Person]=[]):
        self.employees = employees


meta/pure/metamodel/section


class SectionIndex(PackageableElement):

    def __init__(self):


meta/pure/metamodel/dataSpace


class DataSpace(PackageableElement):

    def __init__(self, executionContexts:list[DataSpaceExecutionContext], defaultExecutionContext:DataSpaceExecutionContext, title:str=None, description:str=None, diagrams:list[DataSpaceDiagram]=[], elements:list[PackageableElement]=[], executables:list[DataSpaceExecutable]=[], supportInfo:DataSpaceSupportInfo=None):
        self.executionContexts = executionContexts
        self.defaultExecutionContext = defaultExecutionContext
        self.title = title
        self.description = description
        self.diagrams = diagrams
        self.elements = elements
        self.executables = executables
        self.supportInfo = supportInfo


class DataSpaceExecutionContext(Any):

    def __init__(self, name:str, mapping:Mapping, defaultRuntime:PackageableRuntime, title:str=None, description:str=None, testData:EmbeddedData=None):
        self.name = name
        self.mapping = mapping
        self.defaultRuntime = defaultRuntime
        self.title = title
        self.description = description
        self.testData = testData


class DataSpaceDiagram(Any):

    def __init__(self, title:str, diagram:Diagram, description:str=None):
        self.title = title
        self.diagram = diagram
        self.description = description


class DataSpaceExecutable(Any):

    def __init__(self, title:str, id:str, description:str=None, executionContextKey:str=None):
        self.title = title
        self.id = id
        self.description = description
        self.executionContextKey = executionContextKey


class DataSpacePackageableElementExecutable(DataSpaceExecutable):

    def __init__(self, executable:PackageableElement):
        self.executable = executable


class DataSpaceTemplateExecutable(DataSpaceExecutable):

    def __init__(self, query:FunctionDefinition):
        self.query = query


class DataSpaceSupportInfo(Any):

    def __init__(self, documentationUrl:str=None):
        self.documentationUrl = documentationUrl


class DataSpaceSupportEmail(DataSpaceSupportInfo):

    def __init__(self, address:str):
        self.address = address


class DataSpaceSupportCombinedInfo(DataSpaceSupportInfo):

    def __init__(self, emails:list[str]=[], website:str=None, faqUrl:str=None, supportUrl:str=None):
        self.emails = emails
        self.website = website
        self.faqUrl = faqUrl
        self.supportUrl = supportUrl

meta/pure/metamodel/dataSpace/profiles


meta/pure/metamodel/dataSpace/analytics


class DataSpaceAnalysisResult(Any):

    def __init__(self, diagramModels:DiagramModelCoverageAnalysisResult, executionContexts:list[DataSpaceExecutionContextAnalysisResult]=[], elementDocs:list[DataSpaceModelDocumentationEntry]=[]):
        self.diagramModels = diagramModels
        self.executionContexts = executionContexts
        self.elementDocs = elementDocs


class DataSpaceCoverageAnalysisResult(Any):

    def __init__(self, executionContexts:list[DataSpaceExecutionContextAnalysisResult]=[]):
        self.executionContexts = executionContexts


class DataSpaceExecutionContextAnalysisResult(Any):

    def __init__(self, name:str, mappingCoverage:MappingModelCoverageAnalysisResult, compatibleRuntimes:list[PackageableRuntime]=[]):
        self.name = name
        self.mappingCoverage = mappingCoverage
        self.compatibleRuntimes = compatibleRuntimes


class DataSpaceBasicDocumentationEntry(Any):

    def __init__(self, name:str, docs:list[str]=[]):
        self.name = name
        self.docs = docs


class DataSpacePropertyDocumentationEntry(DataSpaceBasicDocumentationEntry):

    def __init__(self, multiplicity:Multiplicity, milestoning:str=None, type:str=None):
        self.multiplicity = multiplicity
        self.milestoning = milestoning
        self.type = type


class DataSpaceModelDocumentationEntry(DataSpaceBasicDocumentationEntry):

    def __init__(self, element:PackageableElement, path:str):
        self.element = element
        self.path = path


class DataSpaceClassDocumentationEntry(DataSpaceModelDocumentationEntry):

    def __init__(self, properties:list[DataSpacePropertyDocumentationEntry]=[], milestoning:str=None):
        self.properties = properties
        self.milestoning = milestoning


class DataSpaceEnumerationDocumentationEntry(DataSpaceModelDocumentationEntry):

    def __init__(self, enumValues:list[DataSpaceBasicDocumentationEntry]=[]):
        self.enumValues = enumValues


class DataSpaceAssociationDocumentationEntry(DataSpaceModelDocumentationEntry):

    def __init__(self, properties:list[DataSpacePropertyDocumentationEntry]=[]):
        self.properties = properties
