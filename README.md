# pipelines_for_seq_data_trim

This pipelines uses btrim or fqtrim to trim the adapors and low quality bases obtained by SGS.
Default is btrim.
New trim tools will be added in the future up-grade.
### Depend packages
1. btrim: http://graphics.med.yale.edu/trim/
2. fqtrim: https://ccb.jhu.edu/software/fqtrim/
3. python >= 3.6
### Install
* git clone https://github.com/www139516/pipelines_for_seq_data_trim.git
* cd pipelines_for_seq_data_trim
* python your/path/to/pipelines_for_seq_data_trim/main_seq_data_trim.py -d <directory containing fq.gz files>
### For more information, just typing
*python your/path/to/pipelines_for_seq_data_trim/main_seq_data_trim.py --help*
