# -*- coding: utf-8 -*-
#BEGIN_HEADER

from pprint import pprint

from PangenomeFileUtil.PangenomeFileUtilCore import PangenomeDownload

#END_HEADER


class PangenomeFileUtil:
    '''
    Module Name:
    PangenomeFileUtil

    Module Description:
    
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.4"
    GIT_URL = "git@github.com:kbaseapps/PangenomeFileUtilImpl.git"
    GIT_COMMIT_HASH = "19d844e1281c373ce6141f17a9ce2f8ff5f4f8c3"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.pgdnld = PangenomeDownload(config)
        #END_CONSTRUCTOR
        pass

    def pangenome_to_tsv_file(self, ctx, params):
        """
        :param params: instance of type "PangenomeToFileParams" -> structure:
           parameter "pangenome_name" of String, parameter "workspace_name"
           of String
        :returns: instance of type "PangenomeTsvFiles" -> structure:
           parameter "genomes_path" of String, parameter "orthologs_path" of
           String, parameter "shock_id" of String
        """
        # ctx is the context object
        # return variables are: files
        #BEGIN pangenome_to_tsv_file
        print('pangenome_to_tsv_file -- paramaters = ')
        pprint(params)
        self.pgdnld.validate_params(params)
        params['pangenome_ref'] = params['workspace_name'] + "/" + \
                                  params['pangenome_name']
        pg_name, files = self.pgdnld.to_tsv(params)

        #END pangenome_to_tsv_file

        # At some point might do deeper type checking...
        if not isinstance(files, dict):
            raise ValueError('Method pangenome_to_tsv_file return value ' +
                             'files is not type dict as required.')
        # return the results
        return [files]

    def pangenome_to_excel_file(self, ctx, params):
        """
        :param params: instance of type "PangenomeToFileParams" -> structure:
           parameter "pangenome_name" of String, parameter "workspace_name"
           of String
        :returns: instance of type "PangenomeExcelFile" -> structure:
           parameter "path" of String, parameter "shock_id" of String
        """
        # ctx is the context object
        # return variables are: file
        #BEGIN pangenome_to_excel_file
        print('pangenome_to_excel_file -- paramaters = ')
        pprint(params)
        self.pgdnld.validate_params(params)
        params['pangenome_ref'] = params['workspace_name'] + "/" + \
                                  params['pangenome_name']
        pg_name, file = self.pgdnld.to_excel(params)

        #END pangenome_to_excel_file

        # At some point might do deeper type checking...
        if not isinstance(file, dict):
            raise ValueError('Method pangenome_to_excel_file return value ' +
                             'file is not type dict as required.')
        # return the results
        return [file]

    def export_pangenome_as_tsv_file(self, ctx, params):
        """
        :param params: instance of type "ExportParams" -> structure:
           parameter "input_ref" of String
        :returns: instance of type "ExportOutput" -> structure: parameter
           "shock_id" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN export_pangenome_as_tsv_file

        print('export_pangenome_as_tsv_file -- paramaters = ')
        pprint(params)
        self.pgdnld.validate_params(params, {'input_ref'})
        params['pangenome_ref'] = params['input_ref']
        pg_name, files = self.pgdnld.to_tsv(params)
        output = self.pgdnld.export(list(files.values()), pg_name, params)

        #END export_pangenome_as_tsv_file

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method export_pangenome_as_tsv_file return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def export_pangenome_as_excel_file(self, ctx, params):
        """
        :param params: instance of type "ExportParams" -> structure:
           parameter "input_ref" of String
        :returns: instance of type "ExportOutput" -> structure: parameter
           "shock_id" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN export_pangenome_as_excel_file

        print('export_pangenome_as_excel_file -- paramaters = ')
        pprint(params)
        self.pgdnld.validate_params(params, {'input_ref'})
        params['pangenome_ref'] = params['input_ref']
        pg_name, file = self.pgdnld.to_excel(params)
        output = self.pgdnld.export(list(file.values()), pg_name, params)

        #END export_pangenome_as_excel_file

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method export_pangenome_as_excel_file return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
