/*
 * JULEA - Flexible storage framework
 * Copyright (C) 2019-2022 Michael Kuhn
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <julea.h>
#include <julea-object.h>
#include <julea-kv.h>
#include <julea-db.h>

#include <locale.h>
#include <stdio.h>

int
main(int argc, char** argv)
{
	g_autoptr(JBatch) batch = NULL;
	g_autoptr(JDBEntry) entry = NULL;
	g_autoptr(JDBSchema) schema = NULL;
	g_autoptr(JKV) kv = NULL;
	g_autoptr(JObject) object = NULL;

	gchar const* hello_object = "Hello Object!";
	gchar const* hello_kv = "Hello Key-Value!";
	gchar const* hello_database = "Hello Database!";

	guint64 nbytes;

	(void)argc;
	(void)argv;

	// Explicitly enable UTF-8 since functions such as g_format_size might return UTF-8 characters.
	setlocale(LC_ALL, "C.UTF-8");

	/// \todo: this example does not clean up after itself and will only work if the object, kv pair and db entry do not exist already
	/// \todo: add more error checking

	batch = j_batch_new_for_template(J_SEMANTICS_TEMPLATE_DEFAULT);
	object = j_object_new("hello", "world");
	kv = j_kv_new("hello", "world");
	schema = j_db_schema_new("hello", "world", NULL);
	j_db_schema_add_field(schema, "hello", J_DB_TYPE_STRING, NULL);
	entry = j_db_entry_new(schema, NULL);
	j_db_entry_set_field(entry, "hello", hello_database, strlen(hello_database) + 1, NULL);

	j_object_create(object, batch);
	j_object_write(object, hello_object, strlen(hello_object) + 1, 0, &nbytes, batch);
	j_kv_put(kv, g_strdup(hello_kv), strlen(hello_kv) + 1, g_free, batch);
	j_db_schema_create(schema, batch, NULL);
	j_db_entry_insert(entry, batch, NULL);

	if (!j_batch_execute(batch))
	{
		return 1;
	}

	return 0;
}
