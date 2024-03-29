FROM alpine:3.16.3

RUN apk update && apk add gcc g++ make musl-dev python3 python3-dev py3-pip py3-wheel

WORKDIR /src/website-generator

ADD Prebuild.mk requirements.txt .

RUN make -f Prebuild.mk INSTALL_DEPS

ADD . .

RUN make BUILD

CMD ["make", "SERVE"]
