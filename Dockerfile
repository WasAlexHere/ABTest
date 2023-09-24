FROM ubuntu:18.04
RUN mkdir /tests
COPY tester* /test/
CMD ["./test/tester.so", "0.0.0.0", "8080"]