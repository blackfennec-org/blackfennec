from blackfennec_doubles.extension_system.double_extensions.destroy_failing_extension.double_destroy_failing_extension import \
    DestroyFailingExtensionMock

_ = DestroyFailingExtensionMock()
create_extension = _.create_extension
destroy_extension = _.destroy_extension
