package com.formacionbdi.springboot.app.item.models;

import java.util.List;

public interface ItemService {
	public List<item> findAll();
	public item finById(Long id, Integer cantidad);
}
