meta/pure/mapping


class Result(Any):

    def __init__(self, values, activities:list[Activity]=[]):
        self.values = values
        self.activities = activities


class Activity(Any):

    def __init__(self):


class RoutingActivity(Activity):

    def __init__(self, routingTimeInNanoSecond:int=None):
        self.routingTimeInNanoSecond = routingTimeInNanoSecond


class Mapping(PackageableElement,Testable):

    def __init__(self, includes:list[MappingInclude]=[], classMappings:list[SetImplementation]=[], enumerationMappings:list[EnumerationMapping]=[], associationMappings:list[AssociationImplementation]=[]):
        self.includes = includes
        self.classMappings = classMappings
        self.enumerationMappings = enumerationMappings
        self.associationMappings = associationMappings


class ValueTransformer(Any):

    def __init__(self):


class EnumerationMapping(ValueTransformer):

    def __init__(self, name:str, parent:Mapping, enumeration:Enumeration, enumValueMappings:list[EnumValueMapping]=[]):
        self.name = name
        self.parent = parent
        self.enumeration = enumeration
        self.enumValueMappings = enumValueMappings


class EnumValueMapping(Any):

    def __init__(self, enum:Enum, sourceValues:list[Any]=[]):
        self.enum = enum
        self.sourceValues = sourceValues


class PropertyOwnerImplementation(Any):

    def __init__(self, id:str, parent:Mapping, superSetImplementationId:str=None):
        self.id = id
        self.parent = parent
        self.superSetImplementationId = superSetImplementationId


class SetImplementation(PropertyOwnerImplementation):

    def __init__(self, root:bool, class:Class):
        self.root = root
        self.class = class


class PropertyMappingsImplementation(PropertyOwnerImplementation):

    def __init__(self, stores:list[Store]=[], propertyMappings:list[PropertyMapping]=[]):
        self.stores = stores
        self.propertyMappings = propertyMappings


class InstanceSetImplementation(SetImplementation,PropertyMappingsImplementation):

    def __init__(self, mappingClass:MappingClass=None, aggregateSpecification:AggregateSpecification=None):
        self.mappingClass = mappingClass
        self.aggregateSpecification = aggregateSpecification


class EmbeddedSetImplementation(InstanceSetImplementation,PropertyMapping):

    def __init__(self):


class AssociationImplementation(PropertyMappingsImplementation):

    def __init__(self, association:Association):
        self.association = association


class OtherwiseEmbeddedSetImplementation(EmbeddedSetImplementation):

    def __init__(self, otherwisePropertyMapping:PropertyMapping):
        self.otherwisePropertyMapping = otherwisePropertyMapping


class InlineEmbeddedSetImplementation(EmbeddedSetImplementation):

    def __init__(self, inlineSetImplementationId:str):
        self.inlineSetImplementationId = inlineSetImplementationId


class SetImplementationContainer(Any):

    def __init__(self, id:str, setImplementation:SetImplementation):
        self.id = id
        self.setImplementation = setImplementation


class OperationSetImplementation(SetImplementation):

    def __init__(self, operation:Function, parameters:list[SetImplementationContainer]=[]):
        self.operation = operation
        self.parameters = parameters


class MergeOperationSetImplementation(OperationSetImplementation):

    def __init__(self, validationFunction:LambdaFunction):
        self.validationFunction = validationFunction


class PropertyMapping(Any):

    def __init__(self, targetSetImplementationId:str, sourceSetImplementationId:str, property:Property, owner:PropertyMappingsImplementation=None, localMappingProperty:bool=None, localMappingPropertyType:Type=None, localMappingPropertyMultiplicity:Multiplicity=None, store:Store=None):
        self.targetSetImplementationId = targetSetImplementationId
        self.sourceSetImplementationId = sourceSetImplementationId
        self.property = property
        self.owner = owner
        self.localMappingProperty = localMappingProperty
        self.localMappingPropertyType = localMappingPropertyType
        self.localMappingPropertyMultiplicity = localMappingPropertyMultiplicity
        self.store = store


class PropertyMappingValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, propertyMapping:PropertyMapping):
        self.propertyMapping = propertyMapping


class MappingClass(Class):

    def __init__(self, setImplementation:SetImplementation=None, class:Class=None, localProperties:list[Property]=[]):
        self.setImplementation = setImplementation
        self.class = class
        self.localProperties = localProperties


class MappingInclude(Any):

    def __init__(self, owner:Mapping, included:Mapping, storeSubstitutions:list[SubstituteStore]=[]):
        self.owner = owner
        self.included = included
        self.storeSubstitutions = storeSubstitutions


class SubstituteStore(Any):

    def __init__(self, owner:MappingInclude, original:Store, substitute:Store):
        self.owner = owner
        self.original = original
        self.substitute = substitute


class StaticMappingInstanceData(Any):

    def __init__(self, mapping:Mapping, runtime:Runtime, systemMapping:StoreContract, exeCtx:ExecutionContext, debug:DebugContext, setImplementation:InstanceSetImplementation=None, extensions:list[Extension]=[]):
        self.mapping = mapping
        self.runtime = runtime
        self.systemMapping = systemMapping
        self.exeCtx = exeCtx
        self.debug = debug
        self.setImplementation = setImplementation
        self.extensions = extensions


class MappingInstanceData(Any):

    def __init__(self, static:StaticMappingInstanceData, mappingPropertyValues:list[KeyValue]=[]):
        self.static = static
        self.mappingPropertyValues = mappingPropertyValues


class StoreQuery(Any):

    def __init__(self, vs:ValueSpecification, inScopeVars:Map, store:Store):
        self.vs = vs
        self.inScopeVars = inScopeVars
        self.store = store


class TabularDataSetImplementation(TabularDataSet):

    def __init__(self, store:Store):
        self.store = store


class M2MEmbeddedSetImplementation(EmbeddedSetImplementation):

    def __init__(self):
