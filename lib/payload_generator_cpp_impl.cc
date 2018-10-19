/* -*- c++ -*- */
/*
 * Copyright 2018 GENESYS Lab..
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include <gnuradio/blocks/pdu.h>
#include "payload_generator_cpp_impl.h"

namespace gr {
  namespace beamforming {

    payload_generator_cpp::sptr
    payload_generator_cpp::make(std::string file_path , int size)
    {
      return gnuradio::get_initial_sptr
        (new payload_generator_cpp_impl( file_path,  size));
    }

    /*
     * The private constructor
     */
    payload_generator_cpp_impl::payload_generator_cpp_impl(std::string file_path , int size)
      : gr::block("payload_generator_cpp",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(0, 0, 0)
            )
    {

      message_port_register_in(pmt::mp("generate"));

      message_port_register_out(pmt::mp("64QAM_pdu"));
      message_port_register_out(pmt::mp("32QAM_pdu"));
      message_port_register_out(pmt::mp("16QAM_pdu"));
      message_port_register_out(pmt::mp("8QAM_pdu"));
      message_port_register_out(pmt::mp("QPSK_pdu"));
      message_port_register_out(pmt::mp("BSPK_pdu"));


      set_msg_handler(pmt::mp("generate"), boost::bind(&payload_generator_cpp_impl::generate_pdu, this, _1));


    }

    /*
     * Our virtual destructor.
     */
    payload_generator_cpp_impl::~payload_generator_cpp_impl()
    {
    }



    void
    payload_generator_cpp_impl::generate_pdu()
    {
      std::cout<< "Generating payload ... " <<std::endl;

      // fill it with random bytes
      int len = 48;

      //std::vector<unsigned char> vec2(payload_BPSK, payload_BPSK+3);
      //std::vector<unsigned char> vec4(payload_QPSK, payload_QPSK+3);
      std::vector<unsigned char> vec8(payload_8QAM, payload_8QAM+3);
      vec8.insert(vec8.end(), payload_8QAM, payload_8QAM+3);
      std::vector<unsigned char> vec16(payload_16QAM, payload_16QAM+8);
      //std::vector<unsigned char> vec32(payload_32QAM, payload_32QAM+8);
      std::vector<unsigned char> vec64(payload_64QAM, payload_64QAM+len);

      //for (int i=0; i<len; i++)
      //    std::cout<< vec[i] << " - " <<(unsigned int)vec[i] <<std::endl;
      //  vec[i] = ((unsigned char) 191);

      // send the vector
      pmt::pmt_t vecpmt8(pmt::make_blob(&vec8[0], vec8.size()));
      pmt::pmt_t pdu8(pmt::cons(pmt::PMT_NIL, vecpmt8));

      pmt::pmt_t vecpmt16(pmt::make_blob(&vec16[0], vec16.size()));
      pmt::pmt_t pdu16(pmt::cons(pmt::PMT_NIL, vecpmt16));

      pmt::pmt_t vecpmt64(pmt::make_blob(&vec64[0], len));
      pmt::pmt_t pdu64(pmt::cons(pmt::PMT_NIL, vecpmt64));

      message_port_pub( pmt::mp("8QAM_pdu"), pdu8);
      message_port_pub( pmt::mp("16QAM_pdu"), pdu16);
      message_port_pub( pmt::mp("64QAM_pdu"), pdu64);
    }

    void
    payload_generator_cpp_impl::generate_pdu(pmt::pmt_t msg)
    {
      payload_generator_cpp_impl::generate_pdu();
    }


    /* IMPORTANT! Following functions should be used, since this block is not supposed to get any inputs */
    void
    payload_generator_cpp_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
      std::cout<< "This function should not be called";
    }

    int
    payload_generator_cpp_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
    //  const <+ITYPE+> *in = (const <+ITYPE+> *) input_items[0];
    //  <+OTYPE+> *out = (<+OTYPE+> *) output_items[0];

      std::cout<< "This function should not be called";
      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace beamforming */
} /* namespace gr */
