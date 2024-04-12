#include<Python.h>
#include<windows.h>
#include<iostream>
#include<string>
#include<locale>
#include<atlconv.h>
#define PY_SSIZE_T_CLEAN


PyObject* ShowWindowWindows(PyObject* self, PyObject* args) {
	char* parsed_title;
	char* parsed_content;
	try
	{
		int success = PyArg_ParseTuple(args, "ss", &parsed_title, &parsed_content);
		if (!success || !parsed_title || !parsed_content) {
			return NULL;
		}
	}
	catch (const std::exception&)
	{
		return NULL;
	}

	WCHAR* wtitle;
	WCHAR* wcontent;
	USES_CONVERSION;
	wtitle = A2W(parsed_title);
	wcontent = A2W(parsed_content);
	if (!wtitle || !wcontent) {
		return NULL;
	}

	long returnvalue = MessageBox(NULL, wcontent, wtitle, MB_OK | MB_ICONWARNING);
	return PyLong_FromLong(returnvalue);
}


static PyMethodDef PopMethods[] = {
	{"PopWin",(PyCFunction)ShowWindowWindows,METH_VARARGS,"Show Native Windows Popups"},
	{NULL,NULL,0,NULL}
};
static PyModuleDef nativepopup_module = {
	PyModuleDef_HEAD_INIT,"nativepopup","Native Popups",0,PopMethods
};
PyMODINIT_FUNC PyInit_nativepopup() {
	return PyModule_Create(&nativepopup_module);
}