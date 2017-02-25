/*
 * Copyright (c) 2010-2017 Michael Kuhn
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHORS AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

#include <julea-config.h>

#include "julea.h"

#include <juri.h>

gboolean
j_cmd_create (gchar const** arguments, gboolean with_parents)
{
	gboolean ret = TRUE;
	JURI* uri = NULL;
	GError* error = NULL;

	if (j_cmd_arguments_length(arguments) != 1)
	{
		ret = FALSE;
		j_cmd_usage();
		goto end;
	}

	if ((uri = j_uri_new(arguments[0])) == NULL)
	{
		ret = FALSE;
		g_print("Error: Invalid argument “%s”.\n", arguments[0]);
		goto end;
	}

	if (!j_uri_create(uri, with_parents, &error))
	{
		ret = FALSE;
		g_print("Error: %s\n", error->message);
		g_error_free(error);
	}

end:
	if (uri != NULL)
	{
		j_uri_free(uri);
	}

	return ret;
}
