# Package

class Package(PackageableElement):

    def __init__(self, children:list["PackageableElement"]=None,
                 name:str=None,
                 package:"Package"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(name,package,reference_usages,stereotypes,tagged_values)
        self.children = [] if children is None else children

# meta/pure/store/Store

class Store(PackageableElement):

    def __init__(self, includes:list["Store"]=None,
                 name:str=None,
                 package:"Package"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(name,package,reference_usages,stereotypes,tagged_values)
        self.includes = [] if includes is None else includes

# meta/pure/functions/collection/TreeNode

class TreeNode():

    def __init__(self, children_data:list["TreeNode"]=None):
        self.children_data = [] if children_data is None else children_data

# meta/pure/test/Test

class Test():

    def __init__(self, id:str,
                 testable:"Testable"):
        self.id = id
        self.testable = testable

# meta/pure/test/Testable

class Testable():

    def __init__(self, tests:list["Test"]=None):
        self.tests = [] if tests is None else tests

# meta/pure/functions/meta/SourceInformation

class SourceInformation():

    def __init__(self, column:int,
                 end_column:int,
                 end_line:int,
                 line:int,
                 source:str,
                 start_column:int,
                 start_line:int):
        self.source = source
        self.start_line = start_line
        self.start_column = start_column
        self.line = line
        self.column = column
        self.end_line = end_line
        self.end_column = end_column

# meta/pure/metamodel


class Referenceable():

    def __init__(self, reference_usages:list["ReferenceUsage"]=None):
        self.reference_usages = [] if reference_usages is None else reference_usages


class ModelElement(AnnotatedElement):

    def __init__(self, name:str=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(stereotypes,tagged_values)
        self.name = name


class PackageableElement(ModelElement,Referenceable):

    def __init__(self, name:str=None,
                 package:"Package"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        ModelElement.__init__(self,name,stereotypes,tagged_values)
        Referenceable.__init__(self,reference_usages)
        self.package = package


class PropertyOwner(PackageableElement):

    def __init__(self, name:str=None,
                 package:"Package"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(name,package,reference_usages,stereotypes,tagged_values)


class ReferenceUsage():

    def __init__(self, offset:int,
                 owner:"Any",
                 property_name:str):
        self.owner = owner
        self.property_name = property_name
        self.offset = offset

# meta/pure/metamodel/type


class Class(Type,PropertyOwner,ElementWithConstraints,PackageableElement,Testable):

    def __init__(self, constraints:list["Constraint"]=None,
                 generalizations:list["Generalization"]=None,
                 multiplicity_parameters:list["InstanceValue"]=None,
                 name:str=None,
                 original_milestoned_properties:list["Property"]=None,
                 package:"Package"=None,
                 properties:list["Property"]=None,
                 properties_from_associations:list["Property"]=None,
                 qualified_properties:list["QualifiedProperty"]=None,
                 qualified_properties_from_associations:list["QualifiedProperty"]=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 specializations:list["Generalization"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None,
                 tests:list["Test"]=None,
                 type_parameters:list["TypeParameter"]=None,
                 type_variables:list["VariableExpression"]=None):
        Type.__init__(self,generalizations,name,specializations)
        PropertyOwner.__init__(self,name,package,reference_usages,stereotypes,tagged_values)
        ElementWithConstraints.__init__(self,constraints)
        PackageableElement.__init__(self,name,package,reference_usages,stereotypes,tagged_values)
        Testable.__init__(self,tests)
        self.properties = [] if properties is None else properties
        self.original_milestoned_properties = [] if original_milestoned_properties is None else original_milestoned_properties
        self.properties_from_associations = [] if properties_from_associations is None else properties_from_associations
        self.qualified_properties = [] if qualified_properties is None else qualified_properties
        self.qualified_properties_from_associations = [] if qualified_properties_from_associations is None else qualified_properties_from_associations
        self.type_parameters = [] if type_parameters is None else type_parameters
        self.type_variables = [] if type_variables is None else type_variables
        self.multiplicity_parameters = [] if multiplicity_parameters is None else multiplicity_parameters


class Any():

    def __init__(self, classifier_generic_type:"GenericType"=None,
                 element_override:"ElementOverride"=None):
        self.classifier_generic_type = classifier_generic_type
        self.element_override = element_override


class Nil():

    def __init__(self):
        pass


class Type():

    def __init__(self, generalizations:list["Generalization"]=None,
                 name:str=None,
                 specializations:list["Generalization"]=None):
        self.name = name
        self.generalizations = [] if generalizations is None else generalizations
        self.specializations = [] if specializations is None else specializations


class DataType(Type):

    def __init__(self, generalizations:list["Generalization"]=None,
                 name:str=None,
                 specializations:list["Generalization"]=None):
        super().__init__(generalizations,name,specializations)


class Measure(DataType,PackageableElement):

    def __init__(self, canonical_unit:"Unit"=None,
                 generalizations:list["Generalization"]=None,
                 name:str=None,
                 non_canonical_units:list["Unit"]=None,
                 package:"Package"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 specializations:list["Generalization"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        DataType.__init__(self,generalizations,name,specializations)
        PackageableElement.__init__(self,name,package,reference_usages,stereotypes,tagged_values)
        self.canonical_unit = canonical_unit
        self.non_canonical_units = [] if non_canonical_units is None else non_canonical_units


class Unit(DataType,Referenceable):

    def __init__(self, measure:"Measure",
                 conversion_function:"FunctionDefinition"=None,
                 generalizations:list["Generalization"]=None,
                 name:str=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 specializations:list["Generalization"]=None):
        DataType.__init__(self,generalizations,name,specializations)
        Referenceable.__init__(self,reference_usages)
        self.measure = measure
        self.conversion_function = conversion_function


class PrimitiveType(DataType,PackageableElement,ElementWithConstraints):

    def __init__(self, constraints:list["Constraint"]=None,
                 extended:bool=None,
                 generalizations:list["Generalization"]=None,
                 name:str=None,
                 package:"Package"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 specializations:list["Generalization"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None,
                 type_variables:list["VariableExpression"]=None):
        DataType.__init__(self,generalizations,name,specializations)
        PackageableElement.__init__(self,name,package,reference_usages,stereotypes,tagged_values)
        ElementWithConstraints.__init__(self,constraints)
        self.extended = extended
        self.type_variables = [] if type_variables is None else type_variables


class Enumeration(DataType,PackageableElement):

    def __init__(self, values,
                 generalizations:list["Generalization"]=None,
                 name:str=None,
                 package:"Package"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 specializations:list["Generalization"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        DataType.__init__(self,generalizations,name,specializations)
        PackageableElement.__init__(self,name,package,reference_usages,stereotypes,tagged_values)
        self.values = values


class Enum(AnnotatedElement):

    def __init__(self, name:str,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(stereotypes,tagged_values)
        self.name = name


class ElementOverride():

    def __init__(self):
        pass


class GetterOverride(ElementOverride):

    def __init__(self, getter_override_to_many:"Function"=None,
                 getter_override_to_one:"Function"=None,
                 hidden_payload:"Any"=None):
        super().__init__()
        self.getter_override_to_one = getter_override_to_one
        self.getter_override_to_many = getter_override_to_many
        self.hidden_payload = hidden_payload


class FunctionType(Type,Referenceable):

    def __init__(self, return_multiplicity:"Multiplicity",
                 return_type:"GenericType",
                 function:list["Function"]=None,
                 generalizations:list["Generalization"]=None,
                 multiplicity_parameters:list["InstanceValue"]=None,
                 name:str=None,
                 parameters:list["VariableExpression"]=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 specializations:list["Generalization"]=None,
                 type_parameters:list["TypeParameter"]=None):
        Type.__init__(self,generalizations,name,specializations)
        Referenceable.__init__(self,reference_usages)
        self.return_type = return_type
        self.return_multiplicity = return_multiplicity
        self.function = [] if function is None else function
        self.parameters = [] if parameters is None else parameters
        self.type_parameters = [] if type_parameters is None else type_parameters
        self.multiplicity_parameters = [] if multiplicity_parameters is None else multiplicity_parameters


class ConstraintsOverride(ElementOverride):

    def __init__(self, constraints_manager:"Function"=None):
        super().__init__()
        self.constraints_manager = constraints_manager


class ConstraintsGetterOverride(GetterOverride,ConstraintsOverride):

    def __init__(self, constraints_manager:"Function"=None,
                 getter_override_to_many:"Function"=None,
                 getter_override_to_one:"Function"=None,
                 hidden_payload:"Any"=None):
        GetterOverride.__init__(self,getter_override_to_many,getter_override_to_one,hidden_payload)
        ConstraintsOverride.__init__(self,constraints_manager)


class ClassProjection(Class,PackageableElement):

    def __init__(self, projection_specification:"RootRouteNode",
                 constraints:list["Constraint"]=None,
                 generalizations:list["Generalization"]=None,
                 multiplicity_parameters:list["InstanceValue"]=None,
                 name:str=None,
                 original_milestoned_properties:list["Property"]=None,
                 package:"Package"=None,
                 properties:list["Property"]=None,
                 properties_from_associations:list["Property"]=None,
                 qualified_properties:list["QualifiedProperty"]=None,
                 qualified_properties_from_associations:list["QualifiedProperty"]=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 specializations:list["Generalization"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None,
                 tests:list["Test"]=None,
                 type_parameters:list["TypeParameter"]=None,
                 type_variables:list["VariableExpression"]=None):
        Class.__init__(self,constraints,generalizations,multiplicity_parameters,name,name,original_milestoned_properties,package,properties,properties_from_associations,qualified_properties,qualified_properties_from_associations,reference_usages,specializations,stereotypes,tagged_values,tests,type_parameters,type_variables)
        PackageableElement.__init__(self,name,package,reference_usages,stereotypes,tagged_values)
        self.projection_specification = projection_specification

# meta/pure/metamodel/type/generics


class GenericType(Referenceable):

    def __init__(self, multiplicity_arguments:list["Multiplicity"]=None,
                 raw_type:"Type"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 type_arguments:list["GenericType"]=None,
                 type_parameter:"TypeParameter"=None,
                 type_variable_values:list["ValueSpecification"]=None):
        super().__init__(reference_usages)
        self.raw_type = raw_type
        self.type_parameter = type_parameter
        self.type_variable_values = [] if type_variable_values is None else type_variable_values
        self.type_arguments = [] if type_arguments is None else type_arguments
        self.multiplicity_arguments = [] if multiplicity_arguments is None else multiplicity_arguments


class TypeParameter():

    def __init__(self, name:str,
                 contravariant:bool=None,
                 lower_bound:"GenericType"=None,
                 upper_bound:"GenericType"=None):
        self.name = name
        self.contravariant = contravariant
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound


class InferredGenericType(GenericType):

    def __init__(self, multiplicity_arguments:list["Multiplicity"]=None,
                 raw_type:"Type"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 type_arguments:list["GenericType"]=None,
                 type_parameter:"TypeParameter"=None,
                 type_variable_values:list["ValueSpecification"]=None):
        super().__init__(multiplicity_arguments,raw_type,reference_usages,type_arguments,type_parameter,type_variable_values)


# meta/pure/metamodel/treepath


class RouteNode(AnnotatedElement):

    def __init__(self, include_all:str,
                 name:str,
                 type:"GenericType",
                 children:list["PropertyRouteNode"]=None,
                 excluded:list["RouteNodePropertyStub"]=None,
                 included:list["RouteNodePropertyStub"]=None,
                 resolved_properties:list["AbstractProperty"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(stereotypes,tagged_values)
        self.name = name
        self.include_all = include_all
        self.type = type
        self.children = [] if children is None else children
        self.resolved_properties = [] if resolved_properties is None else resolved_properties
        self.included = [] if included is None else included
        self.excluded = [] if excluded is None else excluded


class RootRouteNode(RouteNode):

    def __init__(self, include_all:str,
                 name:str,
                 type:"GenericType",
                 children:list["PropertyRouteNode"]=None,
                 excluded:list["RouteNodePropertyStub"]=None,
                 included:list["RouteNodePropertyStub"]=None,
                 owner:"Any"=None,
                 resolved_properties:list["AbstractProperty"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(include_all,name,type,children,excluded,included,resolved_properties,stereotypes,tagged_values)
        self.owner = owner


class PropertyRouteNode(RouteNode):

    def __init__(self, include_all:str,
                 name:str,
                 property_name:str,
                 root:"RootRouteNode",
                 type:"GenericType",
                 children:list["PropertyRouteNode"]=None,
                 excluded:list["RouteNodePropertyStub"]=None,
                 included:list["RouteNodePropertyStub"]=None,
                 resolved_properties:list["AbstractProperty"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(include_all,name,type,children,excluded,included,resolved_properties,stereotypes,tagged_values)
        self.property_name = property_name
        self.root = root


class RouteNodePropertyStub(AnnotatedElement):

    def __init__(self, owner:"RouteNode",
                 parameters:list["InstanceValue"]=None,
                 property:list["AbstractProperty"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(stereotypes,tagged_values)
        self.owner = owner
        self.property = [] if property is None else property
        self.parameters = [] if parameters is None else parameters


class ExistingPropertyRouteNode(PropertyRouteNode):

    def __init__(self, include_all:str,
                 name:str,
                 property:"RouteNodePropertyStub",
                 property_name:str,
                 root:"RootRouteNode",
                 type:"GenericType",
                 children:list["PropertyRouteNode"]=None,
                 excluded:list["RouteNodePropertyStub"]=None,
                 included:list["RouteNodePropertyStub"]=None,
                 resolved_properties:list["AbstractProperty"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(include_all,name,property_name,root,type,children,excluded,included,resolved_properties,stereotypes,tagged_values)
        self.property = property


class NewPropertyRouteNode(PropertyRouteNode):

    def __init__(self, function_definition:"NewPropertyRouteNodeFunctionDefinition",
                 include_all:str,
                 name:str,
                 property_name:str,
                 root:"RootRouteNode",
                 specifications:list["ValueSpecification"],
                 type:"GenericType",
                 children:list["PropertyRouteNode"]=None,
                 excluded:list["RouteNodePropertyStub"]=None,
                 included:list["RouteNodePropertyStub"]=None,
                 resolved_properties:list["AbstractProperty"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(include_all,name,property_name,root,type,children,excluded,included,resolved_properties,stereotypes,tagged_values)
        self.specifications = specifications
        self.function_definition = function_definition


class NewPropertyRouteNodeFunctionDefinition(FunctionDefinition):

    def __init__(self, expression_sequence:list["ValueSpecification"],
                 owner:"NewPropertyRouteNode",
                 applications:list["FunctionExpression"]=None,
                 function_name:str=None,
                 name:str=None,
                 reference_usages:list["ReferenceUsage"]=None):
        super().__init__(expression_sequence,applications,function_name,name,reference_usages)
        self.owner = owner


class PropertyPathTreeNode(TreeNode):

    def __init__(self, children_data:list["TreeNode"]=None,
                 property:"AbstractProperty"=None):
        super().__init__(children_data)
        self.property = property


# meta/pure/metamodel/constraint


class EnforcementLevel(Enum):
    Error = auto()
    Warn = auto()

class Constraint(ModelElement):

    def __init__(self, function_definition:"FunctionDefinition",
                 enforcement_level:str=None,
                 external_id:str=None,
                 message_function:"FunctionDefinition"=None,
                 name:str=None,
                 owner:str=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(name,stereotypes,tagged_values)
        self.function_definition = function_definition
        self.owner = owner
        self.external_id = external_id
        self.enforcement_level = enforcement_level
        self.message_function = message_function


class ValidatedInstance():

    def __init__(self, instance:"Any",
                 results:list["ValidationResult"]=None):
        self.instance = instance
        self.results = [] if results is None else results


class ValidationResult():

    def __init__(self, constraint:"Constraint",
                 enforcement_level:"EnforcementLevel",
                 ins:"ValidatedInstance",
                 success:bool,
                 message:str=None):
        self.success = success
        self.constraint = constraint
        self.enforcement_level = enforcement_level
        self.ins = ins
        self.message = message


class ConstraintContextInformation():

    def __init__(self, class_:"Class",
                 constraint:"Constraint",
                 enforcement_level:"EnforcementLevel",
                 message:str=None,
                 message_function:"FunctionDefinition"=None):
        self.class_ = class_
        self.constraint = constraint
        self.enforcement_level = enforcement_level
        self.message = message
        self.message_function = message_function


# meta/pure/metamodel/function


class Function(Referenceable):

    def __init__(self, applications:list["FunctionExpression"]=None,
                 function_name:str=None,
                 name:str=None,
                 reference_usages:list["ReferenceUsage"]=None):
        super().__init__(reference_usages)
        self.name = name
        self.function_name = function_name
        self.applications = [] if applications is None else applications


class FunctionDefinition(Function):

    def __init__(self, expression_sequence:list["ValueSpecification"],
                 applications:list["FunctionExpression"]=None,
                 function_name:str=None,
                 name:str=None,
                 reference_usages:list["ReferenceUsage"]=None):
        super().__init__(applications,function_name,name,reference_usages)
        self.expression_sequence = expression_sequence


class PackageableFunction(PackageableElement,Function):

    def __init__(self, applications:list["FunctionExpression"]=None,
                 function_name:str=None,
                 name:str=None,
                 package:"Package"=None,
                 post_constraints:list["Constraint"]=None,
                 pre_constraints:list["Constraint"]=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        PackageableElement.__init__(self,name,package,reference_usages,stereotypes,tagged_values)
        Function.__init__(self,applications,function_name,name,reference_usages)
        self.pre_constraints = [] if pre_constraints is None else pre_constraints
        self.post_constraints = [] if post_constraints is None else post_constraints


class NativeFunction(PackageableFunction):

    def __init__(self, applications:list["FunctionExpression"]=None,
                 function_name:str=None,
                 name:str=None,
                 package:"Package"=None,
                 post_constraints:list["Constraint"]=None,
                 pre_constraints:list["Constraint"]=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(applications,function_name,name,package,post_constraints,pre_constraints,reference_usages,stereotypes,tagged_values)


class ConcreteFunctionDefinition(FunctionDefinition,PackageableFunction,Testable):

    def __init__(self, expression_sequence:list["ValueSpecification"],
                 applications:list["FunctionExpression"]=None,
                 function_name:str=None,
                 name:str=None,
                 package:"Package"=None,
                 post_constraints:list["Constraint"]=None,
                 pre_constraints:list["Constraint"]=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None,
                 tests:list["Test"]=None):
        FunctionDefinition.__init__(self,expression_sequence,applications,function_name,name,reference_usages)
        PackageableFunction.__init__(self,applications,function_name,name,name,package,post_constraints,pre_constraints,reference_usages,stereotypes,tagged_values)
        Testable.__init__(self,tests)


class LambdaFunction(FunctionDefinition):

    def __init__(self, expression_sequence:list["ValueSpecification"],
                 applications:list["FunctionExpression"]=None,
                 function_name:str=None,
                 name:str=None,
                 open_variables:list[str]=None,
                 reference_usages:list["ReferenceUsage"]=None):
        super().__init__(expression_sequence,applications,function_name,name,reference_usages)
        self.open_variables = [] if open_variables is None else open_variables

# meta/pure/metamodel/function/property


class AggregationKind(Enum):
    None = auto()
    Shared = auto()
    Composite = auto()

class AbstractProperty(Function,ModelElement):

    def __init__(self, generic_type:"GenericType",
                 multiplicity:"Multiplicity",
                 owner:"PropertyOwner",
                 applications:list["FunctionExpression"]=None,
                 function_name:str=None,
                 name:str=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        Function.__init__(self,applications,function_name,name,reference_usages)
        ModelElement.__init__(self,name,stereotypes,tagged_values)
        self.generic_type = generic_type
        self.multiplicity = multiplicity
        self.owner = owner


class Property(AbstractProperty):

    def __init__(self, aggregation:"AggregationKind",
                 generic_type:"GenericType",
                 multiplicity:"Multiplicity",
                 owner:"PropertyOwner",
                 applications:list["FunctionExpression"]=None,
                 default_value:"DefaultValue"=None,
                 function_name:str=None,
                 name:str=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(generic_type,multiplicity,owner,applications,function_name,name,reference_usages,stereotypes,tagged_values)
        self.aggregation = aggregation
        self.default_value = default_value


class QualifiedProperty(AbstractProperty,FunctionDefinition):

    def __init__(self, expression_sequence:list["ValueSpecification"],
                 generic_type:"GenericType",
                 id:str,
                 multiplicity:"Multiplicity",
                 owner:"PropertyOwner",
                 applications:list["FunctionExpression"]=None,
                 function_name:str=None,
                 name:str=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        AbstractProperty.__init__(self,generic_type,multiplicity,owner,applications,function_name,name,name,reference_usages,stereotypes,tagged_values)
        FunctionDefinition.__init__(self,expression_sequence,applications,function_name,name,reference_usages)
        self.id = id


class DefaultValue(ModelElement):

    def __init__(self, function_definition:"FunctionDefinition"=None,
                 name:str=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(name,stereotypes,tagged_values)
        self.function_definition = function_definition


# meta/pure/metamodel/relation


class GenericTypeOperationType(Enum):
    Union = auto()
    Difference = auto()
    Subset = auto()
    Equal = auto()

class GenericTypeOperation(GenericType):

    def __init__(self, left:"GenericType",
                 right:"GenericType",
                 type:"GenericTypeOperationType",
                 multiplicity_arguments:list["Multiplicity"]=None,
                 raw_type:"Type"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 type_arguments:list["GenericType"]=None,
                 type_parameter:"TypeParameter"=None,
                 type_variable_values:list["ValueSpecification"]=None):
        super().__init__(multiplicity_arguments,raw_type,reference_usages,type_arguments,type_parameter,type_variable_values)
        self.left = left
        self.right = right
        self.type = type


class RelationType(Type,Referenceable):

    def __init__(self, columns:list["Column"]=None,
                 generalizations:list["Generalization"]=None,
                 name:str=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 specializations:list["Generalization"]=None):
        Type.__init__(self,generalizations,name,specializations)
        Referenceable.__init__(self,reference_usages)
        self.columns = [] if columns is None else columns


class Column(Function):

    def __init__(self, name_wild_card:bool,
                 applications:list["FunctionExpression"]=None,
                 function_name:str=None,
                 name:str=None,
                 reference_usages:list["ReferenceUsage"]=None):
        super().__init__(applications,function_name,name,reference_usages)
        self.name_wild_card = name_wild_card


class Relation():

    def __init__(self):
        pass


class RelationElementAccessor(Relation,Referenceable):

    def __init__(self, source_element:"Any",
                 reference_usages:list["ReferenceUsage"]=None):
        Relation.__init__(self,)
        Referenceable.__init__(self,reference_usages)
        self.source_element = source_element


class ColSpec():

    def __init__(self, name:str):
        self.name = name


class ColSpecArray():

    def __init__(self, names:list[str]=None):
        self.names = [] if names is None else names


class FuncColSpec():

    def __init__(self, function:"Function",
                 name:str):
        self.name = name
        self.function = function


class FuncColSpecArray():

    def __init__(self, func_specs:list["FuncColSpec"]=None):
        self.func_specs = [] if func_specs is None else func_specs


class AggColSpec():

    def __init__(self, map:"Function",
                 name:str,
                 reduce:"Function"):
        self.name = name
        self.map = map
        self.reduce = reduce


class AggColSpecArray():

    def __init__(self, agg_specs:list["AggColSpec"]=None):
        self.agg_specs = [] if agg_specs is None else agg_specs


class TDS(Relation):

    def __init__(self, csv:str):
        super().__init__()
        self.csv = csv


class TDSRelationAccessor(RelationElementAccessor):

    def __init__(self, source_element:"Any",
                 reference_usages:list["ReferenceUsage"]=None):
        super().__init__(source_element,reference_usages)


# meta/pure/metamodel/relationship


class Generalization():

    def __init__(self, general:"GenericType",
                 specific:"Type"):
        self.specific = specific
        self.general = general


class Association(PropertyOwner):

    def __init__(self, name:str=None,
                 original_milestoned_properties:list["Property"]=None,
                 package:"Package"=None,
                 properties:list["Property"]=None,
                 qualified_properties:list["QualifiedProperty"]=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(name,package,reference_usages,stereotypes,tagged_values)
        self.properties = [] if properties is None else properties
        self.original_milestoned_properties = [] if original_milestoned_properties is None else original_milestoned_properties
        self.qualified_properties = [] if qualified_properties is None else qualified_properties


class AssociationProjection(Association):

    def __init__(self, projections:list["ClassProjection"],
                 projected_association:"Association",
                 name:str=None,
                 original_milestoned_properties:list["Property"]=None,
                 package:"Package"=None,
                 properties:list["Property"]=None,
                 qualified_properties:list["QualifiedProperty"]=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(name,original_milestoned_properties,package,properties,qualified_properties,reference_usages,stereotypes,tagged_values)
        self.projections = projections
        self.projected_association = projected_association


# meta/pure/metamodel/valuespecification


class VariableExpression(Expression):

    def __init__(self, generic_type:"GenericType",
                 multiplicity:"Multiplicity",
                 name:str,
                 function_type_owner:"FunctionType"=None,
                 usage_context:"ValueSpecificationContext"=None):
        super().__init__(generic_type,multiplicity,usage_context)
        self.name = name
        self.function_type_owner = function_type_owner


class ValueSpecification():

    def __init__(self, generic_type:"GenericType",
                 multiplicity:"Multiplicity",
                 usage_context:"ValueSpecificationContext"=None):
        self.generic_type = generic_type
        self.multiplicity = multiplicity
        self.usage_context = usage_context


class InstanceValue(ValueSpecification):

    def __init__(self, generic_type:"GenericType",
                 multiplicity:"Multiplicity",
                 usage_context:"ValueSpecificationContext"=None,
                 values:list["Any"]=None):
        super().__init__(generic_type,multiplicity,usage_context)
        self.values = [] if values is None else values


class ValueSpecificationContext():

    def __init__(self, offset:int):
        self.offset = offset


class Expression(ValueSpecification):

    def __init__(self, generic_type:"GenericType",
                 multiplicity:"Multiplicity",
                 usage_context:"ValueSpecificationContext"=None):
        super().__init__(generic_type,multiplicity,usage_context)


class NonExecutableValueSpecification(ValueSpecification):

    def __init__(self, generic_type:"GenericType",
                 multiplicity:"Multiplicity",
                 usage_context:"ValueSpecificationContext"=None,
                 values:list["Any"]=None):
        super().__init__(generic_type,multiplicity,usage_context)
        self.values = [] if values is None else values


class ExpressionSequenceValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, function_definition:"FunctionDefinition",
                 offset:int):
        super().__init__(offset)
        self.function_definition = function_definition


class InstanceValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, instance_value:"InstanceValue",
                 offset:int):
        super().__init__(offset)
        self.instance_value = instance_value


class ClassConstraintValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, offset:int,
                 type:"Type"):
        super().__init__(offset)
        self.type = type


class ParameterValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, function_expression:"FunctionExpression",
                 offset:int):
        super().__init__(offset)
        self.function_expression = function_expression


class FunctionExpression(Expression):

    def __init__(self, func:"Function",
                 generic_type:"GenericType",
                 import_group:"ImportGroup",
                 multiplicity:"Multiplicity",
                 function_name:str=None,
                 original_milestoned_property:"Function"=None,
                 original_milestoned_property_parameters_values:list["ValueSpecification"]=None,
                 parameters_values:list["ValueSpecification"]=None,
                 property_name:"InstanceValue"=None,
                 qualified_property_name:"InstanceValue"=None,
                 resolved_multiplicity_parameters:list["Multiplicity"]=None,
                 resolved_type_parameters:list["GenericType"]=None,
                 usage_context:"ValueSpecificationContext"=None):
        super().__init__(generic_type,multiplicity,usage_context)
        self.func = func
        self.import_group = import_group
        self.parameters_values = [] if parameters_values is None else parameters_values
        self.function_name = function_name
        self.property_name = property_name
        self.qualified_property_name = qualified_property_name
        self.original_milestoned_property = original_milestoned_property
        self.original_milestoned_property_parameters_values = [] if original_milestoned_property_parameters_values is None else original_milestoned_property_parameters_values
        self.resolved_type_parameters = [] if resolved_type_parameters is None else resolved_type_parameters
        self.resolved_multiplicity_parameters = [] if resolved_multiplicity_parameters is None else resolved_multiplicity_parameters


class KeyValueValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, function_expression:"FunctionExpression",
                 offset:int):
        super().__init__(offset)
        self.function_expression = function_expression


class SimpleFunctionExpression(FunctionExpression):

    def __init__(self, func:"Function",
                 generic_type:"GenericType",
                 import_group:"ImportGroup",
                 multiplicity:"Multiplicity",
                 function_name:str=None,
                 original_milestoned_property:"Function"=None,
                 original_milestoned_property_parameters_values:list["ValueSpecification"]=None,
                 parameters_values:list["ValueSpecification"]=None,
                 property_name:"InstanceValue"=None,
                 qualified_property_name:"InstanceValue"=None,
                 resolved_multiplicity_parameters:list["Multiplicity"]=None,
                 resolved_type_parameters:list["GenericType"]=None,
                 usage_context:"ValueSpecificationContext"=None):
        super().__init__(func,generic_type,import_group,multiplicity,function_name,original_milestoned_property,original_milestoned_property_parameters_values,parameters_values,property_name,qualified_property_name,resolved_multiplicity_parameters,resolved_type_parameters,usage_context)


class StoreValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, offset:int,
                 store:"Store"):
        super().__init__(offset)
        self.store = store


# meta/pure/metamodel/multiplicity


class Multiplicity():

    def __init__(self, lower_bound:"MultiplicityValue"=None,
                 multiplicity_parameter:str=None,
                 upper_bound:"MultiplicityValue"=None):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.multiplicity_parameter = multiplicity_parameter


class MultiplicityValue():

    def __init__(self, value:int=None):
        self.value = value


class PackageableMultiplicity(Multiplicity,PackageableElement):

    def __init__(self, lower_bound:"MultiplicityValue"=None,
                 multiplicity_parameter:str=None,
                 name:str=None,
                 package:"Package"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None,
                 upper_bound:"MultiplicityValue"=None):
        Multiplicity.__init__(self,lower_bound,multiplicity_parameter,upper_bound)
        PackageableElement.__init__(self,name,package,reference_usages,stereotypes,tagged_values)


# meta/pure/metamodel/extension


class ElementWithConstraints():

    def __init__(self, constraints:list["Constraint"]=None):
        self.constraints = [] if constraints is None else constraints


class ElementWithStereotypes():

    def __init__(self, stereotypes:list["Stereotype"]=None):
        self.stereotypes = [] if stereotypes is None else stereotypes


class Stereotype(Annotation):

    def __init__(self, profile:"Profile",
                 value:str,
                 model_elements:list["AnnotatedElement"]=None):
        super().__init__(profile,value,model_elements)


class ElementWithTaggedValues():

    def __init__(self, tagged_values:list["TaggedValue"]=None):
        self.tagged_values = [] if tagged_values is None else tagged_values


class TaggedValue():

    def __init__(self, tag:"Tag",
                 value:str):
        self.tag = tag
        self.value = value


class AnnotatedElement(ElementWithStereotypes,ElementWithTaggedValues):

    def __init__(self, stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        ElementWithStereotypes.__init__(self,stereotypes)
        ElementWithTaggedValues.__init__(self,tagged_values)


class Profile(PackageableElement):

    def __init__(self, name:str=None,
                 p___stereotypes:list["Stereotype"]=None,
                 p___tags:list["Tag"]=None,
                 package:"Package"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(name,package,reference_usages,stereotypes,tagged_values)
        self.p___stereotypes = [] if p___stereotypes is None else p___stereotypes
        self.p___tags = [] if p___tags is None else p___tags


class Annotation():

    def __init__(self, profile:"Profile",
                 value:str,
                 model_elements:list["AnnotatedElement"]=None):
        self.profile = profile
        self.value = value
        self.model_elements = [] if model_elements is None else model_elements


class Tag(Annotation):

    def __init__(self, profile:"Profile",
                 value:str,
                 model_elements:list["AnnotatedElement"]=None):
        super().__init__(profile,value,model_elements)


# meta/pure/metamodel/import


class ImportGroup(PackageableElement):

    def __init__(self, imports:list["Import"]=None,
                 name:str=None,
                 package:"Package"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(name,package,reference_usages,stereotypes,tagged_values)
        self.imports = [] if imports is None else imports


class Import():

    def __init__(self, path:str):
        self.path = path


class ImportStub():

    def __init__(self, id_or_path:str,
                 import_group:"ImportGroup",
                 resolved_node:"Any"=None):
        self.import_group = import_group
        self.id_or_path = id_or_path
        self.resolved_node = resolved_node


class PropertyStub():

    def __init__(self, owner:"Class",
                 property_name:str,
                 resolved_property:"AbstractProperty"=None):
        self.owner = owner
        self.property_name = property_name
        self.resolved_property = resolved_property


class EnumStub():

    def __init__(self, enum_name:str,
                 enumeration:"Enumeration",
                 resolved_enum:"Enum"=None):
        self.enumeration = enumeration
        self.enum_name = enum_name
        self.resolved_enum = resolved_enum


# meta/pure/metamodel/path


class Path(Function):

    def __init__(self, path:list["PathElement"],
                 start:"GenericType",
                 applications:list["FunctionExpression"]=None,
                 function_name:str=None,
                 name:str=None,
                 reference_usages:list["ReferenceUsage"]=None):
        super().__init__(applications,function_name,name,reference_usages)
        self.start = start
        self.path = path


class PathElement():

    def __init__(self):
        pass


class CastPathElement(PathElement):

    def __init__(self, type:"GenericType"):
        super().__init__()
        self.type = type


class PropertyPathElement(PathElement):

    def __init__(self, property:"AbstractProperty",
                 parameters:list["ValueSpecification"]=None):
        super().__init__()
        self.property = property
        self.parameters = [] if parameters is None else parameters


# meta/pure/metamodel/text


class Text(PackageableElement):

    def __init__(self, content:str,
                 name:str=None,
                 package:"Package"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None,
                 type:str=None):
        super().__init__(name,package,reference_usages,stereotypes,tagged_values)
        self.content = content
        self.type = type


# meta/pure/metamodel/diagram


class Diagram(PackageableElement):

    def __init__(self, association_views:list["AssociationView"]=None,
                 class_views:list["ClassView"]=None,
                 generalization_views:list["GeneralizationView"]=None,
                 name:str=None,
                 package:"Package"=None,
                 property_views:list["PropertyView"]=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(name,package,reference_usages,stereotypes,tagged_values)
        self.class_views = [] if class_views is None else class_views
        self.association_views = [] if association_views is None else association_views
        self.generalization_views = [] if generalization_views is None else generalization_views
        self.property_views = [] if property_views is None else property_views


class AssociationView(PropertyHolderView):

    def __init__(self, association:"Association",
                 from_:"RelationshipViewEnd",
                 property:"AbstractProperty",
                 to:"RelationshipViewEnd",
                 path:list["Point"]=None):
        super().__init__(from_,property,to,path)
        self.association = association


class PropertyView(PropertyHolderView):

    def __init__(self, from_:"RelationshipViewEnd",
                 property:"AbstractProperty",
                 to:"RelationshipViewEnd",
                 path:list["Point"]=None):
        super().__init__(from_,property,to,path)


class RelationshipView():

    def __init__(self, from_:"RelationshipViewEnd",
                 to:"RelationshipViewEnd",
                 path:list["Point"]=None):
        self.from_ = from_
        self.to = to
        self.path = [] if path is None else path


class GeneralizationView(RelationshipView):

    def __init__(self, from_:"RelationshipViewEnd",
                 to:"RelationshipViewEnd",
                 path:list["Point"]=None):
        super().__init__(from_,to,path)


class PropertyHolderView(RelationshipView):

    def __init__(self, from_:"RelationshipViewEnd",
                 property:"AbstractProperty",
                 to:"RelationshipViewEnd",
                 path:list["Point"]=None):
        super().__init__(from_,to,path)
        self.property = property


class RelationshipViewEnd():

    def __init__(self, class_view:"ClassView"):
        self.class_view = class_view


class PositionedRectangle():

    def __init__(self, position:"Point",
                 rectangle:"Rectangle"):
        self.position = position
        self.rectangle = rectangle


class ClassView(PositionedRectangle):

    def __init__(self, class_:"Class",
                 id:str,
                 position:"Point",
                 rectangle:"Rectangle",
                 hide_properties:bool=None,
                 hide_stereotypes:bool=None,
                 hide_tagged_values:bool=None):
        super().__init__(position,rectangle)
        self.class_ = class_
        self.id = id
        self.hide_properties = hide_properties
        self.hide_tagged_values = hide_tagged_values
        self.hide_stereotypes = hide_stereotypes


class Point():

    def __init__(self, x:float,
                 y:float):
        self.x = x
        self.y = y


class Rectangle():

    def __init__(self, height:float,
                 width:float):
        self.width = width
        self.height = height

# meta/pure/metamodel/diagram/analytics

# meta/pure/metamodel/diagram/analytics/modelCoverage


class DiagramModelCoverageAnalysisResult():

    def __init__(self, associations:list["Association"]=None,
                 classes:list["Class"]=None,
                 enumerations:list["Enumeration"]=None,
                 profiles:list["Profile"]=None):
        self.classes = [] if classes is None else classes
        self.enumerations = [] if enumerations is None else enumerations
        self.associations = [] if associations is None else associations
        self.profiles = [] if profiles is None else profiles


# meta/pure/metamodel/serialization

# meta/pure/metamodel/serialization/grammar


class Configuration():

    def __init__(self, full_path:bool,
                 extensions:list["GrammarExtension"]=None):
        self.full_path = full_path
        self.extensions = [] if extensions is None else extensions


class GrammarExtension():

    def __init__(self, extra_connection_handlers:list["Function"]=None,
                 extra_instance_value_handlers:list["Function"]=None):
        self.extra_connection_handlers = [] if extra_connection_handlers is None else extra_connection_handlers
        self.extra_instance_value_handlers = [] if extra_instance_value_handlers is None else extra_instance_value_handlers


# meta/pure/metamodel/serialization/json


class ShallowPackageableElement():

    def __init__(self, name:str,
                 package:str,
                 source_information:"SourceInformation"):
        self.package = package
        self.name = name
        self.source_information = source_information


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

    def __init__(self, last_name:str):
        self.last_name = last_name


class Firm():

    def __init__(self, employees:list["Person"]=None):
        self.employees = [] if employees is None else employees


# meta/pure/metamodel/section


class SectionIndex(PackageableElement):

    def __init__(self, name:str=None,
                 package:"Package"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 tagged_values:list["TaggedValue"]=None):
        super().__init__(name,package,reference_usages,stereotypes,tagged_values)


# meta/pure/metamodel/dataSpace


class DataSpace(PackageableElement):

    def __init__(self, default_execution_context:"DataSpaceExecutionContext",
                 execution_contexts:list["DataSpaceExecutionContext"],
                 description:str=None,
                 diagrams:list["DataSpaceDiagram"]=None,
                 elements:list["PackageableElement"]=None,
                 executables:list["DataSpaceExecutable"]=None,
                 name:str=None,
                 package:"Package"=None,
                 reference_usages:list["ReferenceUsage"]=None,
                 stereotypes:list["Stereotype"]=None,
                 support_info:"DataSpaceSupportInfo"=None,
                 tagged_values:list["TaggedValue"]=None,
                 title:str=None):
        super().__init__(name,package,reference_usages,stereotypes,tagged_values)
        self.execution_contexts = execution_contexts
        self.default_execution_context = default_execution_context
        self.title = title
        self.description = description
        self.diagrams = [] if diagrams is None else diagrams
        self.elements = [] if elements is None else elements
        self.executables = [] if executables is None else executables
        self.support_info = support_info


class DataSpaceExecutionContext():

    def __init__(self, default_runtime:"PackageableRuntime",
                 mapping:"Mapping",
                 name:str,
                 description:str=None,
                 test_data:"EmbeddedData"=None,
                 title:str=None):
        self.name = name
        self.mapping = mapping
        self.default_runtime = default_runtime
        self.title = title
        self.description = description
        self.test_data = test_data


class DataSpaceDiagram():

    def __init__(self, diagram:"Diagram",
                 title:str,
                 description:str=None):
        self.title = title
        self.diagram = diagram
        self.description = description


class DataSpaceExecutable():

    def __init__(self, id:str,
                 title:str,
                 description:str=None,
                 execution_context_key:str=None):
        self.title = title
        self.id = id
        self.description = description
        self.execution_context_key = execution_context_key


class DataSpacePackageableElementExecutable(DataSpaceExecutable):

    def __init__(self, executable:"PackageableElement",
                 id:str,
                 title:str,
                 description:str=None,
                 execution_context_key:str=None):
        super().__init__(id,title,description,execution_context_key)
        self.executable = executable


class DataSpaceTemplateExecutable(DataSpaceExecutable):

    def __init__(self, id:str,
                 query:"FunctionDefinition",
                 title:str,
                 description:str=None,
                 execution_context_key:str=None):
        super().__init__(id,title,description,execution_context_key)
        self.query = query


class DataSpaceSupportInfo():

    def __init__(self, documentation_url:str=None):
        self.documentation_url = documentation_url


class DataSpaceSupportEmail(DataSpaceSupportInfo):

    def __init__(self, address:str,
                 documentation_url:str=None):
        super().__init__(documentation_url)
        self.address = address


class DataSpaceSupportCombinedInfo(DataSpaceSupportInfo):

    def __init__(self, documentation_url:str=None,
                 emails:list[str]=None,
                 faq_url:str=None,
                 support_url:str=None,
                 website:str=None):
        super().__init__(documentation_url)
        self.emails = [] if emails is None else emails
        self.website = website
        self.faq_url = faq_url
        self.support_url = support_url

# meta/pure/metamodel/dataSpace/profiles


# meta/pure/metamodel/dataSpace/analytics


class DataSpaceAnalysisResult():

    def __init__(self, diagram_models:"DiagramModelCoverageAnalysisResult",
                 element_docs:list["DataSpaceModelDocumentationEntry"]=None,
                 execution_contexts:list["DataSpaceExecutionContextAnalysisResult"]=None):
        self.diagram_models = diagram_models
        self.execution_contexts = [] if execution_contexts is None else execution_contexts
        self.element_docs = [] if element_docs is None else element_docs


class DataSpaceCoverageAnalysisResult():

    def __init__(self, execution_contexts:list["DataSpaceExecutionContextAnalysisResult"]=None):
        self.execution_contexts = [] if execution_contexts is None else execution_contexts


class DataSpaceExecutionContextAnalysisResult():

    def __init__(self, mapping_coverage:"MappingModelCoverageAnalysisResult",
                 name:str,
                 compatible_runtimes:list["PackageableRuntime"]=None):
        self.name = name
        self.mapping_coverage = mapping_coverage
        self.compatible_runtimes = [] if compatible_runtimes is None else compatible_runtimes


class DataSpaceBasicDocumentationEntry():

    def __init__(self, name:str,
                 docs:list[str]=None):
        self.name = name
        self.docs = [] if docs is None else docs


class DataSpacePropertyDocumentationEntry(DataSpaceBasicDocumentationEntry):

    def __init__(self, multiplicity:"Multiplicity",
                 name:str,
                 docs:list[str]=None,
                 milestoning:str=None,
                 type:str=None):
        super().__init__(name,docs)
        self.multiplicity = multiplicity
        self.milestoning = milestoning
        self.type = type


class DataSpaceModelDocumentationEntry(DataSpaceBasicDocumentationEntry):

    def __init__(self, element:"PackageableElement",
                 name:str,
                 path:str,
                 docs:list[str]=None):
        super().__init__(name,docs)
        self.element = element
        self.path = path


class DataSpaceClassDocumentationEntry(DataSpaceModelDocumentationEntry):

    def __init__(self, element:"PackageableElement",
                 name:str,
                 path:str,
                 docs:list[str]=None,
                 milestoning:str=None,
                 properties:list["DataSpacePropertyDocumentationEntry"]=None):
        super().__init__(element,name,path,docs)
        self.properties = [] if properties is None else properties
        self.milestoning = milestoning


class DataSpaceEnumerationDocumentationEntry(DataSpaceModelDocumentationEntry):

    def __init__(self, element:"PackageableElement",
                 name:str,
                 path:str,
                 docs:list[str]=None,
                 enum_values:list["DataSpaceBasicDocumentationEntry"]=None):
        super().__init__(element,name,path,docs)
        self.enum_values = [] if enum_values is None else enum_values


class DataSpaceAssociationDocumentationEntry(DataSpaceModelDocumentationEntry):

    def __init__(self, element:"PackageableElement",
                 name:str,
                 path:str,
                 docs:list[str]=None,
                 properties:list["DataSpacePropertyDocumentationEntry"]=None):
        super().__init__(element,name,path,docs)
        self.properties = [] if properties is None else properties

                   
