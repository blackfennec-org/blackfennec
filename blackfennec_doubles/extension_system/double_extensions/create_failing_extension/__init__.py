from blackfennec_doubles.extension_system.double_extensions.create_failing_extension.double_create_failing_extension import \
    CreateFailingExtensionMock

_ = CreateFailingExtensionMock()
create_extension = _.create_extension
destroy_extension = _.destroy_extension
