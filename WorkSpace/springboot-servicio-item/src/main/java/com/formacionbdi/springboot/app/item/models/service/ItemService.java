package com.formacionbdi.springboot.app.item.models.service;

import java.util.List;

import com.formacionbdi.springboot.app.item.models.item;

public interface ItemService {
	public List<item> findAll();
	public item findById(Long id, Integer cantidad);
}
