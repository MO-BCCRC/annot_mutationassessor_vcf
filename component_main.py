'''

Created on 30 Apr 2015

@author: jrosner

component for annotating vcf files with mutationassessor
'''
from kronos.utils import ComponentAbstract
import os


class Component(ComponentAbstract):

    def __init__(self, component_name='annot_mutationassessor_vcf',
                 component_parent_dir=None, seed_dir=None):

        self.version = '1.0.0'
        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def focus(self, cmd, cmd_args, chunk):
        pass

    def make_cmd(self, chunk=None):
        path = os.path.join(self.seed_dir, 'annotate_mutation_assessor.py')
        cmd = self.requirements['python'] +' '+ path

        cmd_args = ['--vcf '+self.args.vcf,
                    '--output '+self.args.output,
                    '--db '+self.args.db]

        return cmd, cmd_args

    def test(self):
        import component_test
        component_test.run()

def _main():
    comp = Component()
    comp.args = component_ui.args
    comp.run()
    comp.test()


if __name__ == '__main__':
    import component_ui
    _main()
