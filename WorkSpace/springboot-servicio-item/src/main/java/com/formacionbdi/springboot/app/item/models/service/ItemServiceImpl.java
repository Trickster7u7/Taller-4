package com.formacionbdi.springboot.app.item.models.service;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.client.RestTemplate;
import org.springframework.stereotype.Service;

import com.formacionbdi.springboot.app.item.models.item;
import com.formacionbdi.springboot.app.item.models.Producto;

@Service
public class ItemServiceImpl implements ItemService {
	
	@Autowired
	public RestTemplate clienteRest;
	
	
	@Override
	public List<item> findAll() {
		List<Producto> productos = Arrays.asList(clienteRest.getForObject("http://localhost:8001/listar", Producto[].class));
		
		return productos.stream().map( p -> new item (p, 1)).collect(Collectors.toList());
	}

	@Override
	public item findById(Long id, Integer cantidad) {
		Map<String, String> pathVariables = new HashMap<String, String>();
		pathVariables.put("id", id.toString());
		Producto producto = clienteRest.getForObject("http://localhost:8001/ver/{id}", Producto.class, pathVariables);
				return new item(producto, cantidad);
	}

}
