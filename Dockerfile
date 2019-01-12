FROM kbase/sdkbase2:python
MAINTAINER KBase Developer
# -----------------------------------------

RUN pip install pandas && \
    pip install openpyxl && \
    pip install xlrd

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
