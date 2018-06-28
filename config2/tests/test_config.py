
# =========================================
#       DEPS
# --------------------------------------

from os import path

from easypackage.syspath import syspath

syspath()

from attributedict.collections import AttributeDict

from config2.tests import helper
from config2.serializers import yaml_ as yaml

import config2
import config2.config as module

Config = module.Config

deepdict = AttributeDict.dict


# =========================================
#       FIXTURES
# --------------------------------------

package_root_path = helper.root_path()
fixture_foo_root_path = helper.fixture_path('foo')
fixture_foo_src_nested_path = helper.fixture_path('foo', 'src', 'nested')

env_variables_file_basename = 'custom-environment-variables'
env_variables_file_content = helper.fixture('foo/config/{0}.yml'.format(env_variables_file_basename)).read()
env_variables_file_data = yaml.unpack(env_variables_file_content)
env_variables_file = {
    'name': '{0}.yml'.format(env_variables_file_basename),
    'extension': 'yml',
    'format': 'yaml',
    'basename': env_variables_file_basename,
    'raw': env_variables_file_content,
    'path': '{0}/config/{1}.yml'.format(fixture_foo_root_path, env_variables_file_basename),
    'data': env_variables_file_data,
}

default_config_file_basename = 'default'
default_config_file_content = helper.fixture('foo/config/{0}.yml'.format(default_config_file_basename)).read()
default_config_file_data = yaml.unpack(default_config_file_content)
default_config_file = {
    'name': '{0}.yml'.format(default_config_file_basename),
    'extension': 'yml',
    'format': 'yaml',
    'basename': default_config_file_basename,
    'raw': default_config_file_content,
    'path': '{0}/config/{1}.yml'.format(fixture_foo_root_path, default_config_file_basename),
    'data': default_config_file_data,
}

development_config_file_basename = 'development'
development_config_file_content = helper.fixture('foo/config/{0}.yml'.format(development_config_file_basename)).read()
development_config_file_data = yaml.unpack(development_config_file_content)
development_config_file = {
    'name': '{0}.yml'.format(development_config_file_basename),
    'extension': 'yml',
    'format': 'yaml',
    'basename': development_config_file_basename,
    'raw': development_config_file_content,
    'path': '{0}/config/{1}.yml'.format(fixture_foo_root_path, development_config_file_basename),
    'data': development_config_file_data,
}

foo_config_file_basename = 'foo'
foo_config_file_content = helper.fixture('foo/config/{0}.yml'.format(foo_config_file_basename)).read()
foo_config_file_data = yaml.unpack(foo_config_file_content)
foo_config_file = {
    'name': '{0}.yml'.format(foo_config_file_basename),
    'extension': 'yml',
    'format': 'yaml',
    'basename': foo_config_file_basename,
    'raw': foo_config_file_content,
    'path': '{0}/config/{1}.yml'.format(fixture_foo_root_path, foo_config_file_basename),
    'data': foo_config_file_data,
}

production_config_file_basename = 'production'
production_config_file_content = helper.fixture('foo/config/{0}.yml'.format(production_config_file_basename)).read()
production_config_file_data = yaml.unpack(production_config_file_content)
production_config_file = {
    'name': '{0}.yml'.format(production_config_file_basename),
    'extension': 'yml',
    'format': 'yaml',
    'basename': production_config_file_basename,
    'raw': production_config_file_content,
    'path': '{0}/config/{1}.yml'.format(fixture_foo_root_path, production_config_file_basename),
    'data': production_config_file_data,
}

env_config_files = [
    development_config_file,    # development.yml
    foo_config_file,            # foo.yml
    production_config_file,     # production.yml
]

config_files = [
    default_config_file,        # default.yml

    development_config_file,    # development.yml
    foo_config_file,            # foo.yml
    production_config_file,     # production.yml
]

files = [
    env_variables_file,         # custom-environment-variables.yml

    default_config_file,        # default.yml

    development_config_file,    # development.yml
    foo_config_file,            # foo.yml
    production_config_file,     # production.yml
]

default_config_data = default_config_file.get('data')

default_and_development_config_basename = 'default+development'
default_and_development_config_content = helper.fixture('config/{0}.yml'.format(default_and_development_config_basename)).read()
default_and_development_config_data = yaml.unpack(default_and_development_config_content)

default_and_foo_config_basename = 'default+foo'
default_and_foo_config_content = helper.fixture('config/{0}.yml'.format(default_and_foo_config_basename)).read()
default_and_foo_config_data = yaml.unpack(default_and_foo_config_content)

default_and_production_config_basename = 'default+production'
default_and_production_config_content = helper.fixture('config/{0}.yml'.format(default_and_production_config_basename)).read()
default_and_production_config_data = yaml.unpack(default_and_production_config_content)


# =========================================
#       TEST
# --------------------------------------

class TestCase(helper.TestCase):

    def test__import(self):
        self.assertModule(module)

    def test__instance(self):
        self.assertTrue(isinstance(module.Config(), Config))

    def test_env(self):
        self.assertTrue(hasattr(module.Config(), '__env__'))

        config = module.Config()

        self.assertEqual(config.__env__, None)

        config = module.Config('development')

        self.assertEqual(config.__env__, 'development')

        config = module.Config('foo')

        self.assertEqual(config.__env__, 'foo')

        config = module.Config('production')

        self.assertEqual(config.__env__, 'production')

        config = module.Config('xxx')

        self.assertEqual(config.__env__, 'xxx')

    def test_path(self):
        self.assertTrue(hasattr(module.Config(), '__path__'))

        config = module.Config()

        self.assertEqual(config.__path__, package_root_path)

        config = module.Config(path = package_root_path)

        self.assertEqual(config.__path__, package_root_path)

        config = module.Config(path = fixture_foo_root_path)

        self.assertEqual(config.__path__, fixture_foo_root_path)

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertEqual(config.__path__, fixture_foo_src_nested_path)

    def test_root_path(self):
        self.assertTrue(hasattr(module.Config(), '__root_path__'))

        config = module.Config()

        self.assertEqual(config.__root_path__, package_root_path)

        config = module.Config()

        self.assertEqual(config.__root_path__, package_root_path)

        config = module.Config(path = fixture_foo_root_path)

        self.assertEqual(config.__root_path__, fixture_foo_root_path)

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertEqual(config.__root_path__, fixture_foo_root_path)

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertEqual(config.__root_path__, fixture_foo_src_nested_path)

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertEqual(config.__root_path__, fixture_foo_root_path)

    def test_config_path(self):
        self.assertTrue(hasattr(module.Config(), '__config_path__'))

        config = module.Config()

        self.assertEqual(config.__config_path__, path.join(package_root_path, 'config'))

        config = module.Config(path = fixture_foo_root_path)

        self.assertEqual(config.__config_path__, path.join(fixture_foo_root_path, 'config'))

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertEqual(config.__config_path__, path.join(fixture_foo_src_nested_path, 'config'))

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertEqual(config.__config_path__, path.join(fixture_foo_root_path, 'config'))

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertEqual(config.__config_path__, path.join(fixture_foo_root_path, 'config'))

        config = module.Config(path = fixture_foo_root_path, detect = 'not_a_root_file')

        self.assertEqual(config.__config_path__, path.join(package_root_path, 'config'))

        config = module.Config(path = fixture_foo_src_nested_path, detect = 'not_a_root_file')

        self.assertEqual(config.__config_path__, path.join(package_root_path, 'config'))

    def test_config_directory_name(self):
        self.assertTrue(hasattr(module.Config(), '__config_directory_name__'))

        config = module.Config()

        self.assertEqual(config.__config_directory_name__, 'config')

        config = module.Config()

        self.assertEqual(config.__config_directory_name__, 'config')

        config = module.Config(config_directory_name = 'foo')

        self.assertEqual(config.__config_directory_name__, 'foo')
        self.assertEqual(config.__config_path__, path.join(package_root_path, 'foo'))

    def test_config_data(self):
        self.assertTrue(hasattr(module.Config(), '__config_data__'))

        config = module.Config()

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config(detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config(path = package_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config(path = package_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_config_data)

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_config_data)

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_config_data)

        config = module.Config('development')

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('development', path = package_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('development', path = package_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_development_config_data)

        config = module.Config('development', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_development_config_data)

        config = module.Config('development', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('development', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_development_config_data)

        config = module.Config('foo')

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('foo', path = package_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('foo', path = package_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_foo_config_data)

        config = module.Config('foo', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_foo_config_data)

        config = module.Config('foo', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('foo', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_foo_config_data)

        config = module.Config('production')

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('production', path = package_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('production', path = package_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_production_config_data)

        config = module.Config('production', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_production_config_data)

        config = module.Config('production', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('production', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_production_config_data)

        config = module.Config('xxx')

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('xxx', path = package_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('xxx', path = package_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_config_data)

        config = module.Config('xxx', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_config_data)

        config = module.Config('xxx', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__config_data__), None)

        config = module.Config('xxx', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_config_data)

    def test_env_variables_file(self):
        self.assertTrue(hasattr(module.Config(), '__env_variables_file__'))

        config = module.Config()

        self.assertDeepEqual(deepdict(config.__env_variables_file__), None)

        config = module.Config(detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), None)

        config = module.Config(path = package_root_path)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), None)

        config = module.Config(path = package_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), None)

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), None)

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('development')

        self.assertDeepEqual(deepdict(config.__env_variables_file__), None)

        config = module.Config('development', path = package_root_path)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), None)

        config = module.Config('development', path = package_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), None)

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('development', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('development', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), None)

        config = module.Config('development', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

    def test_files(self):
        self.assertTrue(hasattr(module.Config(), '__files__'))

        config = module.Config()

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config(detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config(path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config(path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file]))

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file]))

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file]))

        config = module.Config('development')

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('development', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('development', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, development_config_file]))

        config = module.Config('development', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, development_config_file]))

        config = module.Config('development', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('development', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, development_config_file]))

        config = module.Config('foo')

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('foo', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('foo', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, foo_config_file]))

        config = module.Config('foo', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, foo_config_file]))

        config = module.Config('foo', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('foo', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, foo_config_file]))

        config = module.Config('production')

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('production', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('production', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, production_config_file]))

        config = module.Config('production', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, production_config_file]))

        config = module.Config('production', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('production', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, production_config_file]))

        config = module.Config('xxx')

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('xxx', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('xxx', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file]))

        config = module.Config('xxx', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file]))

        config = module.Config('xxx', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__files__), [])

        config = module.Config('xxx', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file]))

    def test_config_files(self):
        self.assertTrue(hasattr(module.Config(), '__config_files__'))

        config = module.Config()

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config(detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config(path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config(path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file]))

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file]))

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file]))

        config = module.Config('development')

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('development', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('development', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, development_config_file]))

        config = module.Config('development', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, development_config_file]))

        config = module.Config('development', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('development', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, development_config_file]))

        config = module.Config('foo')

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('foo', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('foo', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, foo_config_file]))

        config = module.Config('foo', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, foo_config_file]))

        config = module.Config('foo', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('foo', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, foo_config_file]))

        config = module.Config('production')

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('production', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('production', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, production_config_file]))

        config = module.Config('production', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, production_config_file]))

        config = module.Config('production', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('production', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, production_config_file]))

        config = module.Config('xxx')

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('xxx', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('xxx', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file]))

        config = module.Config('xxx', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file]))

        config = module.Config('xxx', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), [])

        config = module.Config('xxx', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file]))

    def test_default_config_file(self):
        self.assertTrue(hasattr(module.Config(), '__default_config_file__'))

        config = module.Config()

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config(detect = True)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config(path = package_root_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config(path = package_root_path, detect = True)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('development')

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('development', path = package_root_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('development', path = package_root_path, detect = True)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('development', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('development', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('development', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('foo')

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('foo', path = package_root_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('foo', path = package_root_path, detect = True)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('foo', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('foo', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('foo', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('production')

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('production', path = package_root_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('production', path = package_root_path, detect = True)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('production', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('production', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('production', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('xxx')

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('xxx', path = package_root_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('xxx', path = package_root_path, detect = True)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('xxx', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('xxx', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('xxx', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

    def test_env_config_files(self):
        self.assertTrue(hasattr(module.Config(), '__env_config_files__'))

        config = module.Config()

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config(detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config(path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config(path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('development')

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('development', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('development', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('development', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('development', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('development', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('foo')

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('foo', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('foo', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('foo', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('foo', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('foo', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('production')

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('production', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('production', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('production', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('production', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('production', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('xxx')

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('xxx', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('xxx', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('xxx', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('xxx', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), [])

        config = module.Config('xxx', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

    def test_env_variables_file(self):
        self.assertTrue(hasattr(module.Config(), '__env_variables_file__'))

        config = module.Config()

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config(detect = True)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config(path = package_root_path)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config(path = package_root_path, detect = True)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('development')

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('development', path = package_root_path)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('development', path = package_root_path, detect = True)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('development', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('development', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('development', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('foo')

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('foo', path = package_root_path)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('foo', path = package_root_path, detect = True)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('foo', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('foo', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('foo', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('production')

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('production', path = package_root_path)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('production', path = package_root_path, detect = True)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('production', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('production', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('production', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('xxx')

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('xxx', path = package_root_path)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('xxx', path = package_root_path, detect = True)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('xxx', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

        config = module.Config('xxx', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(config.__env_variables_file__, None)

        config = module.Config('xxx', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__env_variables_file__), env_variables_file)

    def test_config(self):
        config = module.Config(path = helper.fixture_path('foo'))

        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['foo', 'bar'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEFAULT 2',
                },
            },
        }))

        config = module.Config('development', path = helper.fixture_path('foo'))

        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['DEV 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEV 2',
                },
            },
            'some_key_only_for_dev': True,
        }))

        config = module.Config('foo', path = helper.fixture_path('foo'))

        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['FOO 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'FOO 2',
                },
            },
            'some_key_only_for_foo': True,
        }))

        config = module.Config('production', path = helper.fixture_path('foo'))

        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['PROD 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'PROD 2',
                },
            },
            'some_key_only_for_prod': True,
        }))

        config = module.Config('xxx', path = helper.fixture_path('foo'))

        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['foo', 'bar'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEFAULT 2',
                },
            },
        }))

    def test_get(self):
        return
        config = module.Config(path = helper.fixture_path('foo'))

        self.assertTrue(hasattr(config, 'get'))

        self.assertDeepEqual(deepdict(config.get()), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['foo', 'bar'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEFAULT 2',
                },
            },
        }))

        config = module.Config('development', path = helper.fixture_path('foo'))

        self.assertEqual(config.__env__, 'development')
        self.assertTrue(isinstance(config.__env_config_file__, dict))
        self.assertTrue(config.__env__ in config.__env_config_file__.path)
        self.assertDeepEqual(deepdict(config.get()), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['DEV 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEV 2',
                },
            },
            'some_key_only_for_dev': True,
        }))

        config = module.Config('foo', path = helper.fixture_path('foo'))

        self.assertEqual(config.__env__, 'foo')
        self.assertTrue(isinstance(config.__env_config_file__, dict))
        self.assertTrue(config.__env__ in config.__env_config_file__.path)
        self.assertDeepEqual(deepdict(config.get()), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['FOO 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'FOO 2',
                },
            },
            'some_key_only_for_foo': True,
        }))

        config = module.Config('production', path = helper.fixture_path('foo'))

        self.assertEqual(config.__env__, 'production')
        self.assertTrue(isinstance(config.__env_config_file__, dict))
        self.assertTrue(config.__env__ in config.__env_config_file__.path)
        self.assertDeepEqual(deepdict(config.get()), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['PROD 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'PROD 2',
                },
            },
            'some_key_only_for_prod': True,
        }))

        config = module.Config('xxx', path = helper.fixture_path('foo'))

        self.assertDeepEqual(deepdict(config.get()), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['foo', 'bar'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEFAULT 2',
                },
            },
        }))

    def test_has(self):
        pass

    def test_config_attribute_get(self):
        pass

    def test_config_attribute_set(self):
        pass

    def test_config_attribute_del(self):
        pass

    def test_config_item_get(self):
        pass

    def test_config_item_set(self):
        pass

    def test_config_item_del(self):
        pass


# =========================================
#       MAIN
# --------------------------------------

if __name__ == '__main__':
    helper.run(TestCase)
