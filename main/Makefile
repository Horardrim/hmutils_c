TARGET = libhmutils-c.so
BUILD_OUTPUT_DIR = ../output

SRC := $(wildcard ./*.c)
OBJS := $(SRC:./%.c=./$(BUILD_OUTPUT_DIR)/%.o)
DEPS := $(SRC:./%.c=./$(BUILD_OUTPUT_DIR)/%.d)

CFLAGS = -g -Wall -Werror -fPIC -shared
INCLUDE_PATH = 
LD_FLAGS =

VERSION = ${HMUTILS_C_VERSION}

all::

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(MAKECMDGOALS),gencov)
ifneq ($(MAKECMDGOALS),package)
-include $(DEPS)
endif
endif
endif

${BUILD_OUTPUT_DIR}/%.d: %.c
	@mkdir -p $(BUILD_OUTPUT_DIR)
	$(CC) -MM -MT "$(BUILD_OUTPUT_DIR)/$(subst .c,.o,${notdir $<}) $(BUILD_OUTPUT_DIR)/$(subst .c,.d,${notdir $<})" -MF "$(subst .c,.d,${BUILD_OUTPUT_DIR}/${notdir $<})" $<

$(BUILD_OUTPUT_DIR)/%.o: %.c
	$(CC) $(CFLAGS) $(INCLUDE_PATH) -c $< -o $@

cov : CFLAGS += -fprofile-arcs -ftest-coverage

cov : LD_FLAGS += -fprofile-arcs -ftest-coverage

cov : all

all:: ${BUILD_OUTPUT_DIR}/${TARGET}

gencov:
	@cp *.c $(BUILD_OUTPUT_DIR)
	@gcov -r -o $(BUILD_OUTPUT_DIR) $(BUILD_OUTPUT_DIR)/*.c

${BUILD_OUTPUT_DIR}/${TARGET}: ${OBJS}
	${CC} ${CFLAGS}  -o $@  $^
	@mv ${BUILD_OUTPUT_DIR}/${TARGET} ${BUILD_OUTPUT_DIR}/${TARGET}.${VERSION}
	@ln -s ${BUILD_OUTPUT_DIR}/${TARGET}.${VERSION} ${BUILD_OUTPUT_DIR}/${TARGET}

clean:
	@rm -rf ${OBJS} ${BUILD_OUTPUT_DIR}/${TARGET} ${DEPS} ${BUILD_OUTPUT_DIR}/${TARGET}.${VERSION}
	@rm -rf hmutils-c-${VERSION}.tar.gz
	@rm -rf hmutils-c-${VERSION}
	@rm -rf ../rpmbuild/SOURCES ../rpmbuild/BUILD  ../rpmbuild/BUILDROOT ../rpmbuild/RPMS ../rpmbuild/SRPMS

package:
	@mkdir -p hmutils-c-${VERSION}
	@cp *.h *.c Makefile hmutils-c-${VERSION}
	@tar -czvf hmutils-c-${VERSION}.tar.gz hmutils-c-${VERSION}
	@mkdir -p ../rpmbuild/SOURCES
	@mv hmutils-c-${VERSION}.tar.gz ../rpmbuild/SOURCES

.PHONY: clean cov gencov package
