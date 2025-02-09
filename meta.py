# meta/pure/metamodel


class PropertyOwner(PackageableElement):

    def __init__(self, package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[]):
        super().__init__(package,name,stereotypes,taggedValues,referenceUsages)


class PackageableElement(ModelElement,Referenceable):

    def __init__(self, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], package:Package=None):
        ModelElement.__init__(name,stereotypes,taggedValues)
        Referenceable.__init__(referenceUsages)
        self.package = package


class Referenceable():

    def __init__(self, referenceUsages:list[ReferenceUsage]=[]):
        self.referenceUsages = referenceUsages


class ModelElement(AnnotatedElement):

    def __init__(self, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], name:str=None):
        super().__init__(stereotypes,taggedValues)
        self.name = name


class ReferenceUsage():

    def __init__(self, owner:Any, propertyName:str, offset:int):
        self.owner = owner
        self.propertyName = propertyName
        self.offset = offset

# meta/pure/metamodel/type


class Class(Type,PropertyOwner,ElementWithConstraints,PackageableElement,Testable):

    def __init__(self, name:str=None, generalizations:list[Generalization]=[], specializations:list[Generalization]=[], package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], constraints:list[Constraint]=[], tests:list[Test]=[], properties:list[Property]=[], originalMilestonedProperties:list[Property]=[], propertiesFromAssociations:list[Property]=[], qualifiedProperties:list[QualifiedProperty]=[], qualifiedPropertiesFromAssociations:list[QualifiedProperty]=[], typeParameters:list[TypeParameter]=[], typeVariables:list[VariableExpression]=[], multiplicityParameters:list[InstanceValue]=[]):
        Type.__init__(name,generalizations,specializations)
        PropertyOwner.__init__(package,name,stereotypes,taggedValues,referenceUsages)
        ElementWithConstraints.__init__(constraints)
        PackageableElement.__init__(package,name,stereotypes,taggedValues,referenceUsages)
        Testable.__init__(tests)
        self.properties = properties
        self.originalMilestonedProperties = originalMilestonedProperties
        self.propertiesFromAssociations = propertiesFromAssociations
        self.qualifiedProperties = qualifiedProperties
        self.qualifiedPropertiesFromAssociations = qualifiedPropertiesFromAssociations
        self.typeParameters = typeParameters
        self.typeVariables = typeVariables
        self.multiplicityParameters = multiplicityParameters


class Nil():

    def __init__(self):
        pass

class Any():

    def __init__(self, classifierGenericType:GenericType=None, elementOverride:ElementOverride=None):
        self.classifierGenericType = classifierGenericType
        self.elementOverride = elementOverride


class Type():

    def __init__(self, name:str=None, generalizations:list[Generalization]=[], specializations:list[Generalization]=[]):
        self.name = name
        self.generalizations = generalizations
        self.specializations = specializations


class DataType(Type):

    def __init__(self, name:str=None, generalizations:list[Generalization]=[], specializations:list[Generalization]=[]):
        super().__init__(name,generalizations,specializations)


class Measure(DataType,PackageableElement):

    def __init__(self, name:str=None, generalizations:list[Generalization]=[], specializations:list[Generalization]=[], package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], canonicalUnit:Unit=None, nonCanonicalUnits:list[Unit]=[]):
        DataType.__init__(name,generalizations,specializations)
        PackageableElement.__init__(package,name,stereotypes,taggedValues,referenceUsages)
        self.canonicalUnit = canonicalUnit
        self.nonCanonicalUnits = nonCanonicalUnits


class Unit(DataType,Referenceable):

    def __init__(self, measure:Measure, name:str=None, generalizations:list[Generalization]=[], specializations:list[Generalization]=[], referenceUsages:list[ReferenceUsage]=[], conversionFunction:FunctionDefinition=None):
        DataType.__init__(name,generalizations,specializations)
        Referenceable.__init__(referenceUsages)
        self.measure = measure
        self.conversionFunction = conversionFunction


class PrimitiveType(DataType,PackageableElement,ElementWithConstraints):

    def __init__(self, name:str=None, generalizations:list[Generalization]=[], specializations:list[Generalization]=[], package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], constraints:list[Constraint]=[], extended:bool=None, typeVariables:list[VariableExpression]=[]):
        DataType.__init__(name,generalizations,specializations)
        PackageableElement.__init__(package,name,stereotypes,taggedValues,referenceUsages)
        ElementWithConstraints.__init__(constraints)
        self.extended = extended
        self.typeVariables = typeVariables


class Enumeration(DataType,PackageableElement):

    def __init__(self, values, name:str=None, generalizations:list[Generalization]=[], specializations:list[Generalization]=[], package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[]):
        DataType.__init__(name,generalizations,specializations)
        PackageableElement.__init__(package,name,stereotypes,taggedValues,referenceUsages)
        self.values = values


class Enum(AnnotatedElement):

    def __init__(self, name:str, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[]):
        super().__init__(stereotypes,taggedValues)
        self.name = name


class ElementOverride():

    def __init__(self):
        pass

class GetterOverride(ElementOverride):

    def __init__(self, getterOverrideToOne:Function=None, getterOverrideToMany:Function=None, hiddenPayload:Any=None):
        super().__init__()
        self.getterOverrideToOne = getterOverrideToOne
        self.getterOverrideToMany = getterOverrideToMany
        self.hiddenPayload = hiddenPayload


class FunctionType(Type,Referenceable):

    def __init__(self, returnType:GenericType, returnMultiplicity:Multiplicity, name:str=None, generalizations:list[Generalization]=[], specializations:list[Generalization]=[], referenceUsages:list[ReferenceUsage]=[], function:list[Function]=[], parameters:list[VariableExpression]=[], typeParameters:list[TypeParameter]=[], multiplicityParameters:list[InstanceValue]=[]):
        Type.__init__(name,generalizations,specializations)
        Referenceable.__init__(referenceUsages)
        self.returnType = returnType
        self.returnMultiplicity = returnMultiplicity
        self.function = function
        self.parameters = parameters
        self.typeParameters = typeParameters
        self.multiplicityParameters = multiplicityParameters


class ConstraintsOverride(ElementOverride):

    def __init__(self, constraintsManager:Function=None):
        super().__init__()
        self.constraintsManager = constraintsManager


class ConstraintsGetterOverride(GetterOverride,ConstraintsOverride):

    def __init__(self, getterOverrideToOne:Function=None, getterOverrideToMany:Function=None, hiddenPayload:Any=None, constraintsManager:Function=None):
        GetterOverride.__init__(getterOverrideToOne,getterOverrideToMany,hiddenPayload)
        ConstraintsOverride.__init__(constraintsManager)


class ClassProjection(Class,PackageableElement):

    def __init__(self, projectionSpecification:RootRouteNode, properties:list[Property]=[], originalMilestonedProperties:list[Property]=[], propertiesFromAssociations:list[Property]=[], qualifiedProperties:list[QualifiedProperty]=[], qualifiedPropertiesFromAssociations:list[QualifiedProperty]=[], typeParameters:list[TypeParameter]=[], typeVariables:list[VariableExpression]=[], multiplicityParameters:list[InstanceValue]=[], name:str=None, generalizations:list[Generalization]=[], specializations:list[Generalization]=[], package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], constraints:list[Constraint]=[], tests:list[Test]=[]):
        Class.__init__(properties,originalMilestonedProperties,propertiesFromAssociations,qualifiedProperties,qualifiedPropertiesFromAssociations,typeParameters,typeVariables,multiplicityParameters,name,generalizations,specializations,package,name,stereotypes,taggedValues,referenceUsages,constraints,tests)
        PackageableElement.__init__(package,name,stereotypes,taggedValues,referenceUsages)
        self.projectionSpecification = projectionSpecification

# meta/pure/metamodel/type/generics


class GenericType(Referenceable):

    def __init__(self, referenceUsages:list[ReferenceUsage]=[], rawType:Type=None, typeParameter:TypeParameter=None, typeVariableValues:list[ValueSpecification]=[], typeArguments:list[GenericType]=[], multiplicityArguments:list[Multiplicity]=[]):
        super().__init__(referenceUsages)
        self.rawType = rawType
        self.typeParameter = typeParameter
        self.typeVariableValues = typeVariableValues
        self.typeArguments = typeArguments
        self.multiplicityArguments = multiplicityArguments


class TypeParameter():

    def __init__(self, name:str, contravariant:bool=None, lowerBound:GenericType=None, upperBound:GenericType=None):
        self.name = name
        self.contravariant = contravariant
        self.lowerBound = lowerBound
        self.upperBound = upperBound


class InferredGenericType(GenericType):

    def __init__(self, rawType:Type=None, typeParameter:TypeParameter=None, typeVariableValues:list[ValueSpecification]=[], typeArguments:list[GenericType]=[], multiplicityArguments:list[Multiplicity]=[], referenceUsages:list[ReferenceUsage]=[]):
        super().__init__(rawType,typeParameter,typeVariableValues,typeArguments,multiplicityArguments,referenceUsages)


# meta/pure/metamodel/treepath


class RootRouteNode(RouteNode):

    def __init__(self, name:str, includeAll:str, type:GenericType, children:list[PropertyRouteNode]=[], resolvedProperties:list[AbstractProperty]=[], included:list[RouteNodePropertyStub]=[], excluded:list[RouteNodePropertyStub]=[], stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], owner:Any=None):
        super().__init__(name,includeAll,type,children,resolvedProperties,included,excluded,stereotypes,taggedValues)
        self.owner = owner


class RouteNode(AnnotatedElement):

    def __init__(self, name:str, includeAll:str, type:GenericType, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], children:list[PropertyRouteNode]=[], resolvedProperties:list[AbstractProperty]=[], included:list[RouteNodePropertyStub]=[], excluded:list[RouteNodePropertyStub]=[]):
        super().__init__(stereotypes,taggedValues)
        self.name = name
        self.includeAll = includeAll
        self.type = type
        self.children = children
        self.resolvedProperties = resolvedProperties
        self.included = included
        self.excluded = excluded


class PropertyRouteNode(RouteNode):

    def __init__(self, name:str, includeAll:str, type:GenericType, propertyName:str, root:RootRouteNode, children:list[PropertyRouteNode]=[], resolvedProperties:list[AbstractProperty]=[], included:list[RouteNodePropertyStub]=[], excluded:list[RouteNodePropertyStub]=[], stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[]):
        super().__init__(name,includeAll,type,children,resolvedProperties,included,excluded,stereotypes,taggedValues)
        self.propertyName = propertyName
        self.root = root


class RouteNodePropertyStub(AnnotatedElement):

    def __init__(self, owner:RouteNode, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], property:list[AbstractProperty]=[], parameters:list[InstanceValue]=[]):
        super().__init__(stereotypes,taggedValues)
        self.owner = owner
        self.property = property
        self.parameters = parameters


class ExistingPropertyRouteNode(PropertyRouteNode):

    def __init__(self, propertyName:str, root:RootRouteNode, name:str, includeAll:str, type:GenericType, property:RouteNodePropertyStub, children:list[PropertyRouteNode]=[], resolvedProperties:list[AbstractProperty]=[], included:list[RouteNodePropertyStub]=[], excluded:list[RouteNodePropertyStub]=[], stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[]):
        super().__init__(propertyName,root,name,includeAll,type,children,resolvedProperties,included,excluded,stereotypes,taggedValues)
        self.property = property


class NewPropertyRouteNode(PropertyRouteNode):

    def __init__(self, propertyName:str, root:RootRouteNode, name:str, includeAll:str, type:GenericType, specifications:list[ValueSpecification], functionDefinition:NewPropertyRouteNodeFunctionDefinition, children:list[PropertyRouteNode]=[], resolvedProperties:list[AbstractProperty]=[], included:list[RouteNodePropertyStub]=[], excluded:list[RouteNodePropertyStub]=[], stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[]):
        super().__init__(propertyName,root,name,includeAll,type,children,resolvedProperties,included,excluded,stereotypes,taggedValues)
        self.specifications = specifications
        self.functionDefinition = functionDefinition


class NewPropertyRouteNodeFunctionDefinition(FunctionDefinition):

    def __init__(self, expressionSequence:list[ValueSpecification], owner:NewPropertyRouteNode, name:str=None, functionName:str=None, applications:list[FunctionExpression]=[], referenceUsages:list[ReferenceUsage]=[]):
        super().__init__(expressionSequence,name,functionName,applications,referenceUsages)
        self.owner = owner


class PropertyPathTreeNode(TreeNode):

    def __init__(self, childrenData:list[TreeNode]=[], property:AbstractProperty=None):
        super().__init__(childrenData)
        self.property = property


# meta/pure/metamodel/constraint


class Constraint(ModelElement):

    def __init__(self, functionDefinition:FunctionDefinition, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], owner:str=None, externalId:str=None, enforcementLevel:str=None, messageFunction:FunctionDefinition=None):
        super().__init__(name,stereotypes,taggedValues)
        self.functionDefinition = functionDefinition
        self.owner = owner
        self.externalId = externalId
        self.enforcementLevel = enforcementLevel
        self.messageFunction = messageFunction


class ValidatedInstance():

    def __init__(self, instance:Any, results:list[ValidationResult]=[]):
        self.instance = instance
        self.results = results


class ValidationResult():

    def __init__(self, success:bool, constraint:Constraint, enforcementLevel:EnforcementLevel, ins:ValidatedInstance, message:str=None):
        self.success = success
        self.constraint = constraint
        self.enforcementLevel = enforcementLevel
        self.ins = ins
        self.message = message


class ConstraintContextInformation():

    def __init__(self, class:Class, constraint:Constraint, enforcementLevel:EnforcementLevel, message:str=None, messageFunction:FunctionDefinition=None):
        self.class = class
        self.constraint = constraint
        self.enforcementLevel = enforcementLevel
        self.message = message
        self.messageFunction = messageFunction


class EnforcementLevel(Enum):
    Error = auto()
    Warn = auto()

# meta/pure/metamodel/function


class FunctionDefinition(Function):

    def __init__(self, expressionSequence:list[ValueSpecification], name:str=None, functionName:str=None, applications:list[FunctionExpression]=[], referenceUsages:list[ReferenceUsage]=[]):
        super().__init__(name,functionName,applications,referenceUsages)
        self.expressionSequence = expressionSequence


class Function(Referenceable):

    def __init__(self, referenceUsages:list[ReferenceUsage]=[], name:str=None, functionName:str=None, applications:list[FunctionExpression]=[]):
        super().__init__(referenceUsages)
        self.name = name
        self.functionName = functionName
        self.applications = applications


class PackageableFunction(PackageableElement,Function):

    def __init__(self, package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], name:str=None, functionName:str=None, applications:list[FunctionExpression]=[], preConstraints:list[Constraint]=[], postConstraints:list[Constraint]=[]):
        PackageableElement.__init__(package,name,stereotypes,taggedValues,referenceUsages)
        Function.__init__(name,functionName,applications,referenceUsages)
        self.preConstraints = preConstraints
        self.postConstraints = postConstraints


class NativeFunction(PackageableFunction):

    def __init__(self, preConstraints:list[Constraint]=[], postConstraints:list[Constraint]=[], package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], name:str=None, functionName:str=None, applications:list[FunctionExpression]=[]):
        super().__init__(preConstraints,postConstraints,package,name,stereotypes,taggedValues,referenceUsages,name,functionName,applications)


class ConcreteFunctionDefinition(FunctionDefinition,PackageableFunction,Testable):

    def __init__(self, expressionSequence:list[ValueSpecification], name:str=None, functionName:str=None, applications:list[FunctionExpression]=[], referenceUsages:list[ReferenceUsage]=[], preConstraints:list[Constraint]=[], postConstraints:list[Constraint]=[], package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], tests:list[Test]=[]):
        FunctionDefinition.__init__(expressionSequence,name,functionName,applications,referenceUsages)
        PackageableFunction.__init__(preConstraints,postConstraints,package,name,stereotypes,taggedValues,referenceUsages,name,functionName,applications)
        Testable.__init__(tests)


class LambdaFunction(FunctionDefinition):

    def __init__(self, expressionSequence:list[ValueSpecification], name:str=None, functionName:str=None, applications:list[FunctionExpression]=[], referenceUsages:list[ReferenceUsage]=[], openVariables:list[str]=[]):
        super().__init__(expressionSequence,name,functionName,applications,referenceUsages)
        self.openVariables = openVariables

# meta/pure/metamodel/function/property


class Property(AbstractProperty):

    def __init__(self, genericType:GenericType, multiplicity:Multiplicity, owner:PropertyOwner, aggregation:AggregationKind, name:str=None, functionName:str=None, applications:list[FunctionExpression]=[], referenceUsages:list[ReferenceUsage]=[], name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], defaultValue:DefaultValue=None):
        super().__init__(genericType,multiplicity,owner,name,functionName,applications,referenceUsages,name,stereotypes,taggedValues)
        self.aggregation = aggregation
        self.defaultValue = defaultValue


class AggregationKind(Enum):
    None = auto()
    Shared = auto()
    Composite = auto()

class QualifiedProperty(AbstractProperty,FunctionDefinition):

    def __init__(self, genericType:GenericType, multiplicity:Multiplicity, owner:PropertyOwner, expressionSequence:list[ValueSpecification], id:str, name:str=None, functionName:str=None, applications:list[FunctionExpression]=[], referenceUsages:list[ReferenceUsage]=[], name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[]):
        AbstractProperty.__init__(genericType,multiplicity,owner,name,functionName,applications,referenceUsages,name,stereotypes,taggedValues)
        FunctionDefinition.__init__(expressionSequence,name,functionName,applications,referenceUsages)
        self.id = id


class DefaultValue(ModelElement):

    def __init__(self, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], functionDefinition:FunctionDefinition=None):
        super().__init__(name,stereotypes,taggedValues)
        self.functionDefinition = functionDefinition


class AbstractProperty(Function,ModelElement):

    def __init__(self, genericType:GenericType, multiplicity:Multiplicity, owner:PropertyOwner, name:str=None, functionName:str=None, applications:list[FunctionExpression]=[], referenceUsages:list[ReferenceUsage]=[], name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[]):
        Function.__init__(name,functionName,applications,referenceUsages)
        ModelElement.__init__(name,stereotypes,taggedValues)
        self.genericType = genericType
        self.multiplicity = multiplicity
        self.owner = owner


# meta/pure/metamodel/relation


class GenericTypeOperationType(Enum):
    Union = auto()
    Difference = auto()
    Subset = auto()
    Equal = auto()

class GenericTypeOperation(GenericType):

    def __init__(self, left:GenericType, right:GenericType, type:GenericTypeOperationType, rawType:Type=None, typeParameter:TypeParameter=None, typeVariableValues:list[ValueSpecification]=[], typeArguments:list[GenericType]=[], multiplicityArguments:list[Multiplicity]=[], referenceUsages:list[ReferenceUsage]=[]):
        super().__init__(rawType,typeParameter,typeVariableValues,typeArguments,multiplicityArguments,referenceUsages)
        self.left = left
        self.right = right
        self.type = type


class RelationType(Type,Referenceable):

    def __init__(self, name:str=None, generalizations:list[Generalization]=[], specializations:list[Generalization]=[], referenceUsages:list[ReferenceUsage]=[], columns:list[Column]=[]):
        Type.__init__(name,generalizations,specializations)
        Referenceable.__init__(referenceUsages)
        self.columns = columns


class Column(Function):

    def __init__(self, nameWildCard:bool, name:str=None, functionName:str=None, applications:list[FunctionExpression]=[], referenceUsages:list[ReferenceUsage]=[]):
        super().__init__(name,functionName,applications,referenceUsages)
        self.nameWildCard = nameWildCard


class Relation():

    def __init__(self):
        pass

class RelationElementAccessor(Relation,Referenceable):

    def __init__(self, sourceElement:Any, referenceUsages:list[ReferenceUsage]=[]):
        Relation.__init__()
        Referenceable.__init__(referenceUsages)
        self.sourceElement = sourceElement


class ColSpec():

    def __init__(self, name:str):
        self.name = name


class ColSpecArray():

    def __init__(self, names:list[str]=[]):
        self.names = names


class FuncColSpec():

    def __init__(self, name:str, function:Function):
        self.name = name
        self.function = function


class FuncColSpecArray():

    def __init__(self, funcSpecs:list[FuncColSpec]=[]):
        self.funcSpecs = funcSpecs


class AggColSpec():

    def __init__(self, name:str, map:Function, reduce:Function):
        self.name = name
        self.map = map
        self.reduce = reduce


class AggColSpecArray():

    def __init__(self, aggSpecs:list[AggColSpec]=[]):
        self.aggSpecs = aggSpecs


class TDS(Relation):

    def __init__(self, csv:str):
        super().__init__()
        self.csv = csv


class TDSRelationAccessor(RelationElementAccessor):

    def __init__(self, sourceElement:Any, referenceUsages:list[ReferenceUsage]=[]):
        super().__init__(sourceElement,referenceUsages)


# meta/pure/metamodel/relationship


class Generalization():

    def __init__(self, specific:Type, general:GenericType):
        self.specific = specific
        self.general = general


class Association(PropertyOwner):

    def __init__(self, package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], properties:list[Property]=[], originalMilestonedProperties:list[Property]=[], qualifiedProperties:list[QualifiedProperty]=[]):
        super().__init__(package,name,stereotypes,taggedValues,referenceUsages)
        self.properties = properties
        self.originalMilestonedProperties = originalMilestonedProperties
        self.qualifiedProperties = qualifiedProperties


class AssociationProjection(Association):

    def __init__(self, projections:list[ClassProjection], projectedAssociation:Association, properties:list[Property]=[], originalMilestonedProperties:list[Property]=[], qualifiedProperties:list[QualifiedProperty]=[], package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[]):
        super().__init__(properties,originalMilestonedProperties,qualifiedProperties,package,name,stereotypes,taggedValues,referenceUsages)
        self.projections = projections
        self.projectedAssociation = projectedAssociation


# meta/pure/metamodel/valuespecification


class VariableExpression(Expression):

    def __init__(self, genericType:GenericType, multiplicity:Multiplicity, name:str, usageContext:ValueSpecificationContext=None, functionTypeOwner:FunctionType=None):
        super().__init__(genericType,multiplicity,usageContext)
        self.name = name
        self.functionTypeOwner = functionTypeOwner


class InstanceValue(ValueSpecification):

    def __init__(self, genericType:GenericType, multiplicity:Multiplicity, usageContext:ValueSpecificationContext=None, values:list[Any]=[]):
        super().__init__(genericType,multiplicity,usageContext)
        self.values = values


class ValueSpecification():

    def __init__(self, genericType:GenericType, multiplicity:Multiplicity, usageContext:ValueSpecificationContext=None):
        self.genericType = genericType
        self.multiplicity = multiplicity
        self.usageContext = usageContext


class ValueSpecificationContext():

    def __init__(self, offset:int):
        self.offset = offset


class Expression(ValueSpecification):

    def __init__(self, genericType:GenericType, multiplicity:Multiplicity, usageContext:ValueSpecificationContext=None):
        super().__init__(genericType,multiplicity,usageContext)


class NonExecutableValueSpecification(ValueSpecification):

    def __init__(self, genericType:GenericType, multiplicity:Multiplicity, usageContext:ValueSpecificationContext=None, values:list[Any]=[]):
        super().__init__(genericType,multiplicity,usageContext)
        self.values = values


class ExpressionSequenceValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, offset:int, functionDefinition:FunctionDefinition):
        super().__init__(offset)
        self.functionDefinition = functionDefinition


class InstanceValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, offset:int, instanceValue:InstanceValue):
        super().__init__(offset)
        self.instanceValue = instanceValue


class ClassConstraintValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, offset:int, type:Type):
        super().__init__(offset)
        self.type = type


class ParameterValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, offset:int, functionExpression:FunctionExpression):
        super().__init__(offset)
        self.functionExpression = functionExpression


class FunctionExpression(Expression):

    def __init__(self, genericType:GenericType, multiplicity:Multiplicity, func:Function, importGroup:ImportGroup, usageContext:ValueSpecificationContext=None, parametersValues:list[ValueSpecification]=[], functionName:str=None, propertyName:InstanceValue=None, qualifiedPropertyName:InstanceValue=None, originalMilestonedProperty:Function=None, originalMilestonedPropertyParametersValues:list[ValueSpecification]=[], resolvedTypeParameters:list[GenericType]=[], resolvedMultiplicityParameters:list[Multiplicity]=[]):
        super().__init__(genericType,multiplicity,usageContext)
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

    def __init__(self, offset:int, functionExpression:FunctionExpression):
        super().__init__(offset)
        self.functionExpression = functionExpression


class SimpleFunctionExpression(FunctionExpression):

    def __init__(self, func:Function, importGroup:ImportGroup, genericType:GenericType, multiplicity:Multiplicity, parametersValues:list[ValueSpecification]=[], functionName:str=None, propertyName:InstanceValue=None, qualifiedPropertyName:InstanceValue=None, originalMilestonedProperty:Function=None, originalMilestonedPropertyParametersValues:list[ValueSpecification]=[], resolvedTypeParameters:list[GenericType]=[], resolvedMultiplicityParameters:list[Multiplicity]=[], usageContext:ValueSpecificationContext=None):
        super().__init__(func,importGroup,genericType,multiplicity,parametersValues,functionName,propertyName,qualifiedPropertyName,originalMilestonedProperty,originalMilestonedPropertyParametersValues,resolvedTypeParameters,resolvedMultiplicityParameters,usageContext)


class StoreValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, offset:int, store:Store):
        super().__init__(offset)
        self.store = store


# meta/pure/metamodel/multiplicity


class Multiplicity():

    def __init__(self, lowerBound:MultiplicityValue=None, upperBound:MultiplicityValue=None, multiplicityParameter:str=None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.multiplicityParameter = multiplicityParameter


class MultiplicityValue():

    def __init__(self, value:int=None):
        self.value = value


class PackageableMultiplicity(Multiplicity,PackageableElement):

    def __init__(self, lowerBound:MultiplicityValue=None, upperBound:MultiplicityValue=None, multiplicityParameter:str=None, package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[]):
        Multiplicity.__init__(lowerBound,upperBound,multiplicityParameter)
        PackageableElement.__init__(package,name,stereotypes,taggedValues,referenceUsages)


# meta/pure/metamodel/extension


class ElementWithConstraints():

    def __init__(self, constraints:list[Constraint]=[]):
        self.constraints = constraints


class ElementWithStereotypes():

    def __init__(self, stereotypes:list[Stereotype]=[]):
        self.stereotypes = stereotypes


class Stereotype(Annotation):

    def __init__(self, profile:Profile, value:str, modelElements:list[AnnotatedElement]=[]):
        super().__init__(profile,value,modelElements)


class ElementWithTaggedValues():

    def __init__(self, taggedValues:list[TaggedValue]=[]):
        self.taggedValues = taggedValues


class TaggedValue():

    def __init__(self, tag:Tag, value:str):
        self.tag = tag
        self.value = value


class AnnotatedElement(ElementWithStereotypes,ElementWithTaggedValues):

    def __init__(self, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[]):
        ElementWithStereotypes.__init__(stereotypes)
        ElementWithTaggedValues.__init__(taggedValues)


class Profile(PackageableElement):

    def __init__(self, package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], p_stereotypes:list[Stereotype]=[], p_tags:list[Tag]=[]):
        super().__init__(package,name,stereotypes,taggedValues,referenceUsages)
        self.p_stereotypes = p_stereotypes
        self.p_tags = p_tags


class Tag(Annotation):

    def __init__(self, profile:Profile, value:str, modelElements:list[AnnotatedElement]=[]):
        super().__init__(profile,value,modelElements)


class Annotation():

    def __init__(self, profile:Profile, value:str, modelElements:list[AnnotatedElement]=[]):
        self.profile = profile
        self.value = value
        self.modelElements = modelElements


# meta/pure/metamodel/import


class ImportGroup(PackageableElement):

    def __init__(self, package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], imports:list[Import]=[]):
        super().__init__(package,name,stereotypes,taggedValues,referenceUsages)
        self.imports = imports


class Import():

    def __init__(self, path:str):
        self.path = path


class ImportStub():

    def __init__(self, importGroup:ImportGroup, idOrPath:str, resolvedNode:Any=None):
        self.importGroup = importGroup
        self.idOrPath = idOrPath
        self.resolvedNode = resolvedNode


class PropertyStub():

    def __init__(self, owner:Class, propertyName:str, resolvedProperty:AbstractProperty=None):
        self.owner = owner
        self.propertyName = propertyName
        self.resolvedProperty = resolvedProperty


class EnumStub():

    def __init__(self, enumeration:Enumeration, enumName:str, resolvedEnum:Enum=None):
        self.enumeration = enumeration
        self.enumName = enumName
        self.resolvedEnum = resolvedEnum


# meta/pure/metamodel/path


class Path(Function):

    def __init__(self, start:GenericType, path:list[PathElement], name:str=None, functionName:str=None, applications:list[FunctionExpression]=[], referenceUsages:list[ReferenceUsage]=[]):
        super().__init__(name,functionName,applications,referenceUsages)
        self.start = start
        self.path = path


class PathElement():

    def __init__(self):
        pass

class CastPathElement(PathElement):

    def __init__(self, type:GenericType):
        super().__init__()
        self.type = type


class PropertyPathElement(PathElement):

    def __init__(self, property:AbstractProperty, parameters:list[ValueSpecification]=[]):
        super().__init__()
        self.property = property
        self.parameters = parameters


# meta/pure/metamodel/text


class Text(PackageableElement):

    def __init__(self, content:str, package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], type:str=None):
        super().__init__(package,name,stereotypes,taggedValues,referenceUsages)
        self.content = content
        self.type = type


# meta/pure/metamodel/diagram


class Diagram(PackageableElement):

    def __init__(self, package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], classViews:list[ClassView]=[], associationViews:list[AssociationView]=[], generalizationViews:list[GeneralizationView]=[], propertyViews:list[PropertyView]=[]):
        super().__init__(package,name,stereotypes,taggedValues,referenceUsages)
        self.classViews = classViews
        self.associationViews = associationViews
        self.generalizationViews = generalizationViews
        self.propertyViews = propertyViews


class AssociationView(PropertyHolderView):

    def __init__(self, property:AbstractProperty, from:RelationshipViewEnd, to:RelationshipViewEnd, association:Association, path:list[Point]=[]):
        super().__init__(property,from,to,path)
        self.association = association


class PropertyView(PropertyHolderView):

    def __init__(self, property:AbstractProperty, from:RelationshipViewEnd, to:RelationshipViewEnd, path:list[Point]=[]):
        super().__init__(property,from,to,path)


class GeneralizationView(RelationshipView):

    def __init__(self, from:RelationshipViewEnd, to:RelationshipViewEnd, path:list[Point]=[]):
        super().__init__(from,to,path)


class PropertyHolderView(RelationshipView):

    def __init__(self, from:RelationshipViewEnd, to:RelationshipViewEnd, property:AbstractProperty, path:list[Point]=[]):
        super().__init__(from,to,path)
        self.property = property


class RelationshipView():

    def __init__(self, from:RelationshipViewEnd, to:RelationshipViewEnd, path:list[Point]=[]):
        self.from = from
        self.to = to
        self.path = path


class RelationshipViewEnd():

    def __init__(self, classView:ClassView):
        self.classView = classView


class ClassView(PositionedRectangle):

    def __init__(self, position:Point, rectangle:Rectangle, class:Class, id:str, hideProperties:bool=None, hideTaggedValues:bool=None, hideStereotypes:bool=None):
        super().__init__(position,rectangle)
        self.class = class
        self.id = id
        self.hideProperties = hideProperties
        self.hideTaggedValues = hideTaggedValues
        self.hideStereotypes = hideStereotypes


class Point():

    def __init__(self, x:Number, y:Number):
        self.x = x
        self.y = y


class Rectangle():

    def __init__(self, width:Number, height:Number):
        self.width = width
        self.height = height


class PositionedRectangle():

    def __init__(self, position:Point, rectangle:Rectangle):
        self.position = position
        self.rectangle = rectangle

# meta/pure/metamodel/diagram/analytics

# meta/pure/metamodel/diagram/analytics/modelCoverage


class DiagramModelCoverageAnalysisResult():

    def __init__(self, classes:list[Class]=[], enumerations:list[Enumeration]=[], associations:list[Association]=[], profiles:list[Profile]=[]):
        self.classes = classes
        self.enumerations = enumerations
        self.associations = associations
        self.profiles = profiles


# meta/pure/metamodel/serialization

# meta/pure/metamodel/serialization/grammar


class Configuration():

    def __init__(self, fullPath:bool, extensions:list[GrammarExtension]=[]):
        self.fullPath = fullPath
        self.extensions = extensions


class GrammarExtension():

    def __init__(self, extraConnectionHandlers:list[Function]=[], extraInstanceValueHandlers:list[Function]=[]):
        self.extraConnectionHandlers = extraConnectionHandlers
        self.extraInstanceValueHandlers = extraInstanceValueHandlers


# meta/pure/metamodel/serialization/json


class ShallowPackageableElement():

    def __init__(self, package:str, name:str, sourceInformation:SourceInformation):
        self.package = package
        self.name = name
        self.sourceInformation = sourceInformation


# meta/pure/metamodel/tests

# meta/pure/metamodel/tests/namespace


# meta/pure/metamodel/tests/lambda


class Person():

    def __init__(self):
        pass

class Person2():

    def __init__(self, name:str):
        self.name = name


class Employee(Person):

    def __init__(self):
        super().__init__()


class C():

    def __init__(self):
        pass

class Firm():

    def __init__(self, prop:str):
        self.prop = prop


# meta/pure/metamodel/tests/inference


class A():

    def __init__(self, val):
        self.val = val


# meta/pure/metamodel/tests/functionmatching


# meta/pure/metamodel/tests/lambdaopenvariables


class Person():

    def __init__(self, lastName:str):
        self.lastName = lastName


class Firm():

    def __init__(self, employees:list[Person]=[]):
        self.employees = employees


# meta/pure/metamodel/section


class SectionIndex(PackageableElement):

    def __init__(self, package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[]):
        super().__init__(package,name,stereotypes,taggedValues,referenceUsages)


# meta/pure/metamodel/dataSpace


class DataSpace(PackageableElement):

    def __init__(self, executionContexts:list[DataSpaceExecutionContext], defaultExecutionContext:DataSpaceExecutionContext, package:Package=None, name:str=None, stereotypes:list[Stereotype]=[], taggedValues:list[TaggedValue]=[], referenceUsages:list[ReferenceUsage]=[], title:str=None, description:str=None, diagrams:list[DataSpaceDiagram]=[], elements:list[PackageableElement]=[], executables:list[DataSpaceExecutable]=[], supportInfo:DataSpaceSupportInfo=None):
        super().__init__(package,name,stereotypes,taggedValues,referenceUsages)
        self.executionContexts = executionContexts
        self.defaultExecutionContext = defaultExecutionContext
        self.title = title
        self.description = description
        self.diagrams = diagrams
        self.elements = elements
        self.executables = executables
        self.supportInfo = supportInfo


class DataSpaceExecutionContext():

    def __init__(self, name:str, mapping:Mapping, defaultRuntime:PackageableRuntime, title:str=None, description:str=None, testData:EmbeddedData=None):
        self.name = name
        self.mapping = mapping
        self.defaultRuntime = defaultRuntime
        self.title = title
        self.description = description
        self.testData = testData


class DataSpaceDiagram():

    def __init__(self, title:str, diagram:Diagram, description:str=None):
        self.title = title
        self.diagram = diagram
        self.description = description


class DataSpaceExecutable():

    def __init__(self, title:str, id:str, description:str=None, executionContextKey:str=None):
        self.title = title
        self.id = id
        self.description = description
        self.executionContextKey = executionContextKey


class DataSpacePackageableElementExecutable(DataSpaceExecutable):

    def __init__(self, title:str, id:str, executable:PackageableElement, description:str=None, executionContextKey:str=None):
        super().__init__(title,id,description,executionContextKey)
        self.executable = executable


class DataSpaceTemplateExecutable(DataSpaceExecutable):

    def __init__(self, title:str, id:str, query:FunctionDefinition, description:str=None, executionContextKey:str=None):
        super().__init__(title,id,description,executionContextKey)
        self.query = query


class DataSpaceSupportInfo():

    def __init__(self, documentationUrl:str=None):
        self.documentationUrl = documentationUrl


class DataSpaceSupportEmail(DataSpaceSupportInfo):

    def __init__(self, address:str, documentationUrl:str=None):
        super().__init__(documentationUrl)
        self.address = address


class DataSpaceSupportCombinedInfo(DataSpaceSupportInfo):

    def __init__(self, documentationUrl:str=None, emails:list[str]=[], website:str=None, faqUrl:str=None, supportUrl:str=None):
        super().__init__(documentationUrl)
        self.emails = emails
        self.website = website
        self.faqUrl = faqUrl
        self.supportUrl = supportUrl

# meta/pure/metamodel/dataSpace/profiles


# meta/pure/metamodel/dataSpace/analytics


class DataSpaceAnalysisResult():

    def __init__(self, diagramModels:DiagramModelCoverageAnalysisResult, executionContexts:list[DataSpaceExecutionContextAnalysisResult]=[], elementDocs:list[DataSpaceModelDocumentationEntry]=[]):
        self.diagramModels = diagramModels
        self.executionContexts = executionContexts
        self.elementDocs = elementDocs


class DataSpaceCoverageAnalysisResult():

    def __init__(self, executionContexts:list[DataSpaceExecutionContextAnalysisResult]=[]):
        self.executionContexts = executionContexts


class DataSpaceExecutionContextAnalysisResult():

    def __init__(self, name:str, mappingCoverage:MappingModelCoverageAnalysisResult, compatibleRuntimes:list[PackageableRuntime]=[]):
        self.name = name
        self.mappingCoverage = mappingCoverage
        self.compatibleRuntimes = compatibleRuntimes


class DataSpaceBasicDocumentationEntry():

    def __init__(self, name:str, docs:list[str]=[]):
        self.name = name
        self.docs = docs


class DataSpacePropertyDocumentationEntry(DataSpaceBasicDocumentationEntry):

    def __init__(self, name:str, multiplicity:Multiplicity, docs:list[str]=[], milestoning:str=None, type:str=None):
        super().__init__(name,docs)
        self.multiplicity = multiplicity
        self.milestoning = milestoning
        self.type = type


class DataSpaceModelDocumentationEntry(DataSpaceBasicDocumentationEntry):

    def __init__(self, name:str, element:PackageableElement, path:str, docs:list[str]=[]):
        super().__init__(name,docs)
        self.element = element
        self.path = path


class DataSpaceClassDocumentationEntry(DataSpaceModelDocumentationEntry):

    def __init__(self, element:PackageableElement, path:str, name:str, docs:list[str]=[], properties:list[DataSpacePropertyDocumentationEntry]=[], milestoning:str=None):
        super().__init__(element,path,name,docs)
        self.properties = properties
        self.milestoning = milestoning


class DataSpaceEnumerationDocumentationEntry(DataSpaceModelDocumentationEntry):

    def __init__(self, element:PackageableElement, path:str, name:str, docs:list[str]=[], enumValues:list[DataSpaceBasicDocumentationEntry]=[]):
        super().__init__(element,path,name,docs)
        self.enumValues = enumValues


class DataSpaceAssociationDocumentationEntry(DataSpaceModelDocumentationEntry):

    def __init__(self, element:PackageableElement, path:str, name:str, docs:list[str]=[], properties:list[DataSpacePropertyDocumentationEntry]=[]):
        super().__init__(element,path,name,docs)
        self.properties = properties
